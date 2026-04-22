"""Command-line interface for Dorkator.

The CLI orchestrates 3 phases:
    1. Load the YAML library                    (`core.load_library`)
    2. Render the dorks against the target      (`core.build_dorks`)
    3. Output: file export(s) (HTML/MD/JSON) and/or batch open in the browser
       (`opener.open_batches`)

Phase 3 is optional and combinable: you can both generate an HTML report
AND open the "critical" dorks in the browser in a single invocation.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .core import build_dorks, list_categories, load_library
from .exporters import export_html, export_json, export_markdown
from .opener import open_batches

# Path to the dorks.yaml shipped with the package. Resolved via __file__ so it
# still works when the package is installed elsewhere on disk.
DEFAULT_DORKS = Path(__file__).parent.parent / "dorks.yaml"

# Banner is built from __version__ so it stays in sync with the package.
BANNER = rf"""
 ____             _         _
|  _ \  ___  _ __| | ____ _| |_ ___  _ __
| | | |/ _ \| '__| |/ / _` | __/ _ \| '__|
| |_| | (_) | |  |   < (_| | || (_) | |
|____/ \___/|_|  |_|\_\__,_|\__\___/|_|
                                       v{__version__}
"""

# Quick-reference cheatsheet shown under the banner when the user runs
# `dorkator` with no target (instead of the bare argparse error).
QUICK_HELP = """\
Common commands:
  dorkator --list-categories                                  Show categories & dork count
  dorkator -t example.com                                     Generate HTML report
  dorkator -t example.com -f all -o report                    Generate HTML + Markdown + JSON
  dorkator -t example.com -c credentials,technical            Limit to specific categories
  dorkator -t example.com --open --open-severity critical     Browse criticals interactively
  dorkator -t example.com -f none --open --open-batch 10      Open in batches of 10, no file
  dorkator --help                                             Full options reference

Tip: in interactive --open mode, press Enter to advance, 's' to stop, 'q' to quit.
Reminder: only run against assets you own or are authorized to assess.
"""

# Valid severities — used to validate --open-severity input
VALID_SEVERITIES = {"critical", "high", "medium", "low", "info"}


def _parse_severities(raw: str | None) -> set[str] | None:
    """Turn "critical,high" into {"critical","high"}.

    Returns None when the option was not given (= all severities).
    Raises an explicit error if any unknown severity is passed.
    """
    if not raw:
        return None
    parts = {p.strip().lower() for p in raw.split(",") if p.strip()}
    invalid = parts - VALID_SEVERITIES
    if invalid:
        raise argparse.ArgumentTypeError(
            f"invalid severities: {sorted(invalid)}. "
            f"Expected one of: {sorted(VALID_SEVERITIES)}"
        )
    return parts


def _positive_int(raw: str) -> int:
    """argparse type for a strictly positive integer (>= 1)."""
    try:
        value = int(raw)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected an integer, got {raw!r}")
    if value < 1:
        raise argparse.ArgumentTypeError(
            f"expected an integer >= 1, got {value}"
        )
    return value


def _non_negative_float(raw: str) -> float:
    """argparse type for a float >= 0 (a negative pause would crash sleep)."""
    try:
        value = float(raw)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected a number, got {raw!r}")
    if value < 0:
        raise argparse.ArgumentTypeError(
            f"expected a number >= 0, got {value}"
        )
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="dorkator",
        description="OSINT dork generator for authorized reconnaissance.",
        epilog=(
            "Use responsibly. Only run against assets you own or are "
            "authorized to assess."
        ),
    )

    # ---- Target / category selection ------------------------------------
    parser.add_argument(
        "-t", "--target",
        help="Target domain or search term (e.g. example.com).",
    )
    parser.add_argument(
        "-c", "--category",
        help="Comma-separated categories (default: all). See --list-categories.",
    )

    # ---- File output ----------------------------------------------------
    parser.add_argument(
        "-o", "--output",
        default="report",
        help="Output file prefix (default: report).",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["html", "markdown", "json", "all", "none"],
        default="html",
        help=(
            "Output format (default: html). Use 'none' to skip file export "
            "(handy combined with --open to open without writing a file)."
        ),
    )

    # ---- Library --------------------------------------------------------
    parser.add_argument(
        "--dorks",
        default=str(DEFAULT_DORKS),
        help="Path to dorks YAML library (default: bundled dorks.yaml).",
    )
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="List available categories and exit.",
    )

    # ---- Batch opener ---------------------------------------------------
    # All --open-* flags are only effective when --open is set.
    parser.add_argument(
        "--open",
        action="store_true",
        help=(
            "Open the dorks in the browser, in interactive batches. "
            "Combine with --open-severity to open only critical/high."
        ),
    )
    parser.add_argument(
        "--open-engine",
        choices=["google", "ddg", "bing"],
        default="google",
        help="Search engine for --open (default: google).",
    )
    parser.add_argument(
        "--open-batch",
        type=_positive_int,
        default=5,
        metavar="N",
        help=(
            "Number of tabs opened per batch (default: 5, must be >= 1). "
            "The bigger, the higher the captcha risk."
        ),
    )
    parser.add_argument(
        "--open-pause",
        type=_non_negative_float,
        default=2.0,
        metavar="SEC",
        help="Pause (seconds) between two batches (default: 2.0, must be >= 0).",
    )
    parser.add_argument(
        "--open-severity",
        type=_parse_severities,
        default=None,
        metavar="LIST",
        help=(
            "Severities to open, e.g. 'critical,high'. "
            "Default: all."
        ),
    )
    parser.add_argument(
        "--open-no-confirm",
        action="store_true",
        help=(
            "Non-interactive mode: skip the start confirmation and the "
            "between-batches prompt (only the --open-pause delay remains). "
            "Use with care."
        ),
    )

    # ---- Misc -----------------------------------------------------------
    parser.add_argument(
        "--version",
        action="version",
        version=f"dorkator {__version__}",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress the banner.",
    )

    args = parser.parse_args(argv)

    if not args.quiet:
        # Banner on stderr so it doesn't pollute a piped stdout
        print(BANNER, file=sys.stderr)

    # --- Phase 1: load the library --------------------------------------
    library = load_library(Path(args.dorks))

    # --- Special case: --list-categories short-circuits everything ------
    if args.list_categories:
        cats = list_categories(library)
        print(f"{'KEY':<14} {'COUNT':<7} NAME")
        print("-" * 60)
        for c in cats:
            print(f"{c['key']:<14} {c['count']:<7} {c['name']}")
        # Total at the bottom — useful when extending the library
        total = sum(c["count"] for c in cats)
        print("-" * 60)
        print(f"{'TOTAL':<14} {total:<7}")
        return 0

    # --- Validation: a target is required to render dorks ---------------
    # When no target is given, show the quick-help cheatsheet under the banner
    # rather than the bare argparse error. More useful for new users.
    if not args.target:
        if not args.quiet:
            print(QUICK_HELP, file=sys.stderr)
        print(
            "[!] --target is required (unless using --list-categories)",
            file=sys.stderr,
        )
        return 2

    # --- Phase 2: render dorks against the target -----------------------
    categories = (
        [c.strip() for c in args.category.split(",")] if args.category else None
    )
    dorks = build_dorks(library, args.target, categories)

    if not dorks:
        print("No dorks matched your selection.", file=sys.stderr)
        return 1

    # --- Phase 3a: file exports -----------------------------------------
    prefix = Path(args.output)
    fmt = args.format

    if fmt in ("html", "all"):
        out = prefix.with_suffix(".html")
        export_html(dorks, args.target, out)
        print(f"[+] HTML report  -> {out}")
    if fmt in ("markdown", "all"):
        out = prefix.with_suffix(".md")
        export_markdown(dorks, args.target, out)
        print(f"[+] Markdown     -> {out}")
    if fmt in ("json", "all"):
        out = prefix.with_suffix(".json")
        export_json(dorks, args.target, out)
        print(f"[+] JSON         -> {out}")

    print(f"[=] {len(dorks)} dorks generated for '{args.target}'")

    # --- Phase 3b: optional batch open in the browser -------------------
    if args.open:
        open_batches(
            dorks,
            engine=args.open_engine,
            batch_size=args.open_batch,
            pause=args.open_pause,
            interactive=not args.open_no_confirm,
            severities=args.open_severity,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
