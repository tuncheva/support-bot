"""Product catalog loading and search."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from support_bot.config import products_path


@dataclass(frozen=True)
class ProductCatalog:
    products: list[dict[str, Any]]

    @classmethod
    def load(cls, path: Path | None = None) -> "ProductCatalog":
        p = path or products_path()
        try:
            with p.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                data = []
        except Exception:
            data = []
        return cls(products=data)

    def search(self, keyword: str) -> list[dict[str, Any]]:
        """Case-insensitive substring match against name/description/category."""

        if not keyword:
            return []
        kw = keyword.lower()
        results: list[dict[str, Any]] = []
        for p in self.products:
            if (
                kw in str(p.get("name", "")).lower()
                or kw in str(p.get("description", "")).lower()
                or kw in str(p.get("category", "")).lower()
            ):
                results.append(p)
        return results


_DEFAULT_CATALOG = ProductCatalog.load()


def file_search_products(keyword: str) -> list[dict[str, Any]]:
    """Backwards-compatible function wrapper."""

    return _DEFAULT_CATALOG.search(keyword)
