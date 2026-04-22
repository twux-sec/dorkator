"""Interactive wizard — asks 4 questions to build a Dorkator run.

Designed for users who don't want to remember every CLI flag. The wizard
returns a dict that `cli.py` then maps onto the equivalent argparse fields.

Wizard flow:
    Q1. Target (domain or keyword)
    Q2. Categories (all / comma-separated keys)
    Q3. Action (file output / open in browser / both)
    Q4. Severity filter for the browser open (only asked if open is selected)

The wizard is pure I/O — no networking, no side effects beyond stdout/stdin.
"""
from __future__ import annotations

import sys
from typing import Iterable

from .core import list_categories


def _ask(
    question: str,
    *,
    default: str | None = None,
    choices: Iterable[str] | None = None,
) -> str:
    """Prompt the user. Re-prompts on empty answer (unless `default` is set)
    or on a value outside `choices`.

    Ctrl-C / EOF cleanly aborts the wizard with exit code 0.
    """
    choice_list = list(choices) if choices else None
    # Build the suffix: "(a/b/c) [default]"
    parts = []
    if choice_list:
        parts.append(f"({'/'.join(choice_list)})")
    if default is not None:
        parts.append(f"[{default}]")
    suffix = (" " + " ".join(parts)) if parts else ""

    while True:
        try:
            ans = input(f"{question}{suffix}: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[*] Wizard cancelled.", file=sys.stderr)
            sys.exit(0)

        # Empty answer + no default -> re-ask
        if not ans:
            if default is not None:
                return default
            print("  Required.", file=sys.stderr)
            continue

        # Validate against the allowed choices, if any
        if choice_list and ans.lower() not in [c.lower() for c in choice_list]:
            print(f"  Please choose one of: {choice_list}", file=sys.stderr)
            continue

        return ans


def run_wizard(library: dict) -> dict:
    """Run the 4-question wizard.

    Args:
        library: the loaded dorks YAML library (used to list categories in Q2).

    Returns:
        A dict with keys: target, category, do_file, do_open, severity.
        - target:   str
        - category: str | None  (None means "all")
        - do_file:  bool        (True if HTML report should be generated)
        - do_open:  bool        (True if --open should be triggered)
        - severity: str | None  (comma-separated severities, or None for all)
    """
    print("\n--- Dorkator interactive wizard (Ctrl-C to abort) ---\n")

    # ---- Q1: target -----------------------------------------------------
    target = _ask("Q1. Target domain or keyword (e.g. example.com)")

    # ---- Q2: categories -------------------------------------------------
    cats = list_categories(library)
    print("\n  Available categories:")
    for c in cats:
        print(f"    - {c['key']:14} ({c['count']:>3} dorks)  {c['name']}")
    sel = _ask(
        "Q2. Categories: 'all' or comma-separated keys (e.g. credentials,technical)",
        default="all",
    )
    category = None if sel.lower() == "all" else sel

    # ---- Q3: action -----------------------------------------------------
    # f = file only, o = open only, b = both
    action = _ask(
        "Q3. Action: (f)ile report, (o)pen in browser, (b)oth",
        default="b",
        choices=["f", "o", "b"],
    ).lower()
    do_file = action in ("f", "b")
    do_open = action in ("o", "b")

    # ---- Q4: severity (only if browser open is involved) ---------------
    severity = None
    if do_open:
        sev = _ask(
            "Q4. Severities to open: 'all' or comma-separated (e.g. critical,high)",
            default="critical,high",
        )
        severity = None if sev.lower() == "all" else sev

    print()  # blank line before the run output

    return {
        "target": target,
        "category": category,
        "do_file": do_file,
        "do_open": do_open,
        "severity": severity,
    }
