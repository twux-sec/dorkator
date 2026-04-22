"""Export dorks as HTML, Markdown, or JSON."""
from __future__ import annotations

import json
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .core import Dork

TEMPLATES_DIR = Path(__file__).parent / "templates"


@lru_cache(maxsize=1)
def _jinja_env() -> Environment:
    """Build (once) and reuse the Jinja2 environment.

    Caching matters when callers export to multiple formats / targets in the
    same process: re-creating the environment + reparsing the template each
    time is wasteful.

    autoescape: enabled for any html template (incl. .html.j2). Without this,
    quotes in dork queries (e.g. intext:"@target") would close HTML attribute
    boundaries and silently truncate the data-raw-query payload — breaking
    the live rewrite on the static site.
    """
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(
            enabled_extensions=("html", "htm", "xml", "j2", "html.j2"),
            default=True,
        ),
    )


def _group_by_category(dorks: Sequence[Dork]) -> dict[str, dict]:
    """Group already-sorted dorks by category, preserving order."""
    categories: dict[str, dict] = {}
    for d in dorks:
        categories.setdefault(
            d.category,
            {"name": d.category_name, "dorks": []},
        )["dorks"].append(d)
    return categories


def export_html(dorks: Sequence[Dork], target: str, output: Path) -> None:
    """Render a self-contained HTML report with filtering."""
    template = _jinja_env().get_template("report.html.j2")
    html = template.render(
        target=target,
        categories=_group_by_category(dorks),
        total=len(dorks),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    output.write_text(html, encoding="utf-8")


def export_markdown(dorks: Sequence[Dork], target: str, output: Path) -> None:
    """Render a Markdown report (great for Obsidian)."""
    lines = [
        f"# Dorkator Report — `{target}`",
        "",
        f"- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Total dorks:** {len(dorks)}",
        "",
        "> Legal notice: only run against domains you own or are authorized to assess.",
        "",
    ]
    current_cat = None
    for d in dorks:
        if d.category != current_cat:
            lines.append(f"\n## {d.category_name}\n")
            current_cat = d.category
        lines.append(f"### `[{d.severity.upper()}]` {d.name}")
        lines.append("")
        lines.append(f"```\n{d.query}\n```")
        lines.append(
            f"[Google]({d.google_url}) · "
            f"[DuckDuckGo]({d.duckduckgo_url}) · "
            f"[Bing]({d.bing_url})"
        )
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


def export_json(dorks: Sequence[Dork], target: str, output: Path) -> None:
    """Render a JSON payload for downstream tooling."""
    payload = {
        "target": target,
        "generated_at": datetime.now().isoformat(),
        "total": len(dorks),
        "dorks": [d.to_dict() for d in dorks],
    }
    output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def export_static_site(library: dict, output: Path) -> None:
    """Render a standalone interactive HTML site (no fixed target).

    Unlike `export_html`, this output ships every dork with its raw
    `{target}` placeholder. The page contains an input and a small JS
    block that rewrites every query and rebuilds the search-engine URLs
    on each keystroke. Suitable for hosting on GitHub Pages: one HTML
    file, no backend, no build step at view time.
    """
    template = _jinja_env().get_template("static_site.html.j2")

    # Reshape the YAML library into a render-friendly list-of-dicts so the
    # template never has to call methods on dataclass objects.
    categories = []
    for cat_key, cat_data in library["categories"].items():
        categories.append({
            "key": cat_key,
            "name": cat_data.get("name", cat_key),
            "dorks": [
                {
                    "name": d["name"],
                    "query": d["query"],          # keeps {target} verbatim
                    "severity": d.get("severity", "info"),
                }
                for d in cat_data.get("dorks", [])
            ],
        })

    total = sum(len(c["dorks"]) for c in categories)
    html = template.render(
        categories=categories,
        total=total,
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    output.write_text(html, encoding="utf-8")
