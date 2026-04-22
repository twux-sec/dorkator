"""Export dorks as HTML, Markdown, or JSON."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .core import Dork

TEMPLATES_DIR = Path(__file__).parent / "templates"


def _group_by_category(dorks: Sequence[Dork]) -> dict[str, dict]:
    categories: dict[str, dict] = {}
    for d in dorks:
        categories.setdefault(
            d.category,
            {"name": d.category_name, "dorks": []},
        )["dorks"].append(d)
    return categories


def export_html(dorks: Sequence[Dork], target: str, output: Path) -> None:
    """Render a self-contained HTML report with filtering."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    template = env.get_template("report.html.j2")
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
