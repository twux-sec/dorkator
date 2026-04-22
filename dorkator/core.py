"""Core logic for Dorkator: loading and building dorks."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote_plus

import yaml

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}


@dataclass
class Dork:
    """A single dork entry, ready to be rendered against a target."""

    category: str
    category_name: str
    name: str
    query: str
    severity: str
    description: str = ""

    @property
    def google_url(self) -> str:
        return f"https://www.google.com/search?q={quote_plus(self.query)}"

    @property
    def duckduckgo_url(self) -> str:
        return f"https://duckduckgo.com/?q={quote_plus(self.query)}"

    @property
    def bing_url(self) -> str:
        return f"https://www.bing.com/search?q={quote_plus(self.query)}"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["google_url"] = self.google_url
        d["duckduckgo_url"] = self.duckduckgo_url
        d["bing_url"] = self.bing_url
        return d


def load_library(yaml_path: Path) -> dict:
    """Load the dork library from a YAML file."""
    with yaml_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_dorks(
    library: dict,
    target: str,
    categories: Iterable[str] | None = None,
) -> list[Dork]:
    """Render all dorks against the target, optionally filtered by categories."""
    selected = set(categories) if categories else None
    dorks: list[Dork] = []
    for cat_key, cat_data in library["categories"].items():
        if selected and cat_key not in selected:
            continue
        for entry in cat_data.get("dorks", []):
            query = entry["query"].replace("{target}", target)
            dorks.append(
                Dork(
                    category=cat_key,
                    category_name=cat_data.get("name", cat_key),
                    name=entry["name"],
                    query=query,
                    severity=entry.get("severity", "info"),
                    description=entry.get("description", ""),
                )
            )
    dorks.sort(key=lambda d: (SEVERITY_ORDER.get(d.severity, 99), d.category, d.name))
    return dorks


def list_categories(library: dict) -> list[dict]:
    """Return metadata about all categories in the library."""
    return [
        {
            "key": k,
            "name": v.get("name", k),
            "description": v.get("description", ""),
            "count": len(v.get("dorks", [])),
        }
        for k, v in library["categories"].items()
    ]
