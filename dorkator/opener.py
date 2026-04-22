"""Batch opener — opens dorks in the browser, one controlled batch at a time.

Why batches?
    Google triggers captchas if you fire 30 searches in 2 seconds. By opening
    5 tabs at a time and waiting for the user to validate the next batch, we
    keep the user in the driver's seat and stay below Google's rate-limit radar.

Why `webbrowser` (stdlib) rather than Selenium / Playwright?
    `webbrowser.open_new_tab(url)` reuses the user's existing browser (with
    their session, cookies, extensions). That's exactly what we want for
    manual OSINT: the human reads the results. Selenium would imply browser
    automation — i.e. scraping — which would break the "passive tool" promise
    in the README.
"""
from __future__ import annotations

import sys
import time
import webbrowser
from typing import Iterable

from .core import Dork


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _url_for(dork: Dork, engine: str) -> str:
    """Return the ready-to-open URL for the requested engine.

    We support 3 engines: Google (default, richest dork syntax),
    DuckDuckGo (fewer captchas but slightly less expressive), and Bing
    (useful for sites Google indexes poorly).
    """
    if engine == "google":
        return dork.google_url
    if engine == "ddg":
        return dork.duckduckgo_url
    if engine == "bing":
        return dork.bing_url
    raise ValueError(f"Unknown engine: {engine!r} (expected: google, ddg, bing)")


def _filter_for_open(
    dorks: list[Dork],
    severities: set[str] | None,
) -> list[Dork]:
    """Filter the dork list by severities.

    The severity-based ordering is already done upstream by `core.build_dorks`,
    so we preserve it — criticals get opened first.
    """
    if not severities:
        return list(dorks)
    return [d for d in dorks if d.severity in severities]


def _confirm_start(total: int, batch_size: int, engine: str) -> bool:
    """Anti-flood guardrail: ask before opening N tabs.

    Anything other than "y" / "yes" / "" (Enter) cancels. Deliberately strict
    to avoid accidental browser floods (80 dorks = 80 tabs).
    """
    nb_batches = (total + batch_size - 1) // batch_size  # ceil division
    print(
        f"\n[?] About to open {total} dork(s) on {engine} "
        f"({nb_batches} batch(es) of {batch_size}). Continue? [Y/n] ",
        end="",
        file=sys.stderr,
        flush=True,
    )
    try:
        rep = input().strip().lower()
    except EOFError:
        # No stdin available (e.g. piped invocation): cancel by default
        return False
    return rep in ("", "y", "yes")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def open_batches(
    dorks: list[Dork],
    *,
    engine: str = "google",
    batch_size: int = 5,
    pause: float = 2.0,
    interactive: bool = True,
    severities: Iterable[str] | None = None,
) -> int:
    """Open the dorks in the browser, in batches of `batch_size`.

    Args:
        dorks: pre-sorted list returned by `core.build_dorks`.
        engine: "google" | "ddg" | "bing".
        batch_size: number of tabs opened at once before pausing.
        pause: seconds to wait between two batches (on top of confirmation).
        interactive: if True, prompt [Enter/s/q] between each batch.
        severities: set of severities to open (e.g. {"critical","high"}).
                    None = all.

    Returns:
        Number of dorks actually sent to the browser.
    """
    sev_set = set(severities) if severities else None
    selected = _filter_for_open(dorks, sev_set)

    if not selected:
        print(
            "[!] No dork matches the open filters "
            f"(severities={sev_set}).",
            file=sys.stderr,
        )
        return 0

    # Guardrail: never fire 80 tabs without confirming
    if interactive and not _confirm_start(len(selected), batch_size, engine):
        print("[*] Cancelled by user.", file=sys.stderr)
        return 0

    total = len(selected)
    opened = 0
    total_batches = (total + batch_size - 1) // batch_size

    print(
        f"[*] Opening {total} dork(s) on {engine}, "
        f"batches of {batch_size}, {pause}s pause between batches.",
        file=sys.stderr,
    )

    # `range(0, total, batch_size)` yields 0, batch_size, 2*batch_size, ...
    # which gives us non-overlapping contiguous slices of `selected`.
    for start in range(0, total, batch_size):
        batch = selected[start : start + batch_size]
        batch_num = start // batch_size + 1

        print(
            f"\n[batch {batch_num}/{total_batches}] opening "
            f"{len(batch)} tab(s)...",
            file=sys.stderr,
        )

        for d in batch:
            url = _url_for(d, engine)
            # Readable trace so the user can see what's leaving for the browser
            print(
                f"  [{d.severity:>8}] {d.category}: {d.name}",
                file=sys.stderr,
            )
            webbrowser.open_new_tab(url)
            opened += 1
            # 300 ms between tabs: avoids browser race conditions where
            # some tabs would silently fail to open at all
            time.sleep(0.3)

        # Unless we just finished, pause and (optionally) ask for confirmation
        is_last_batch = start + batch_size >= total
        if not is_last_batch:
            time.sleep(pause)
            if interactive:
                try:
                    print(
                        "[?] Enter=next batch, s=stop now, q=quit > ",
                        end="",
                        file=sys.stderr,
                        flush=True,
                    )
                    choice = input().strip().lower()
                except EOFError:
                    # Stdin closed: stop cleanly
                    choice = "q"

                if choice in ("q", "quit", "s", "stop"):
                    print("[*] Stopped on user request.", file=sys.stderr)
                    break

    print(f"\n[=] {opened} dork(s) opened in total.", file=sys.stderr)
    return opened
