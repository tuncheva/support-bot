"""Product catalog loading and search."""

from __future__ import annotations

import json
import re
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

    def _normalize_bulgarian(self, word: str) -> str:
        """Remove Bulgarian articles and case endings for matching.
        
        Handles definite articles: та (the-fem), то (the-neut), ят (the-pl), ът (the-masc)
        Also removes common adjective endings: ски, на, ен
        """
        word = word.lower()
        
        # Try removing definite articles first (longer patterns first)
        # These are the most common article patterns
        article_endings = [
            'та',    # feminine definite: четката (the toothbrush) -> четк
            'ята',   # feminine definite variant
            'ято',   # neuter variant
            'то',    # neuter definite: одеялото (the blanket) -> одеял
            'ятo',   # plural variant
            'ят',    # plural definite
            'ът',    # masculine definite: генераторът (the generator) -> генератор
            'ьт',    # masculine variant
        ]
        
        # Try each article ending, removing only one
        for ending in article_endings:
            if word.endswith(ending) and len(word) > len(ending) + 1:
                return word[:-len(ending)]
        
        # If no article found, try removing common adjective/descriptor endings
        # but only if word is long enough
        descriptor_endings = ['ски', 'на', 'ен', 'ни', 'я']
        for ending in sorted(descriptor_endings, key=len, reverse=True):
            if word.endswith(ending) and len(word) > len(ending) + 3:
                return word[:-len(ending)]
        
        return word

    def search(self, keyword: str, language: str = "en") -> list[dict[str, Any]]:
        """Case-insensitive substring match against name/description/category.
        
        Supports English and Bulgarian (language='en' or language='bg').
        For multi-word queries, scores products by how many keywords they match.
        """

        if not keyword:
            return []
        
        # Determine which fields to search based on language
        name_field = "name_bg" if language == "bg" else "name"
        desc_field = "description_bg" if language == "bg" else "description"
        
        # Split keyword into individual words for multi-word matching
        keywords = keyword.split()
        
        # Normalize keywords (especially for Bulgarian morphology)
        if language == "bg":
            normalized_keywords = [self._normalize_bulgarian(kw) for kw in keywords]
        else:
            normalized_keywords = [kw.lower() for kw in keywords]
        
        results_with_scores: list[tuple[dict[str, Any], int]] = []
        
        for p in self.products:
            name_text = str(p.get(name_field, "")).lower()
            desc_text = str(p.get(desc_field, "")).lower()
            category_text = str(p.get("category", "")).lower()
            full_text = f"{name_text} {desc_text} {category_text}"
            
            # Normalize the product text for Bulgarian
            if language == "bg":
                # Normalize words in the product text
                name_words = re.findall(r'[\u0400-\u04FF]+', name_text)
                desc_words = re.findall(r'[\u0400-\u04FF]+', desc_text)
                normalized_product_text = " ".join(
                    [self._normalize_bulgarian(w) for w in name_words + desc_words]
                )
                normalized_product_text += " " + full_text  # Keep original too for fallback
            else:
                normalized_product_text = full_text
            
            # Score: count how many keywords match
            match_count = 0
            for norm_kw in normalized_keywords:
                if norm_kw in normalized_product_text:
                    match_count += 1
            
            # Include products that match at least one keyword
            if match_count > 0:
                # Boost score for exact substring matches in original text
                bonus = 0
                for orig_kw in keywords:
                    if orig_kw.lower() in full_text:
                        bonus += 2
                results_with_scores.append((p, match_count + bonus))
        
        # Sort by match count (descending), keeping original order for ties
        results_with_scores.sort(key=lambda x: x[1], reverse=True)
        results = [p for p, _ in results_with_scores]
        return results


_DEFAULT_CATALOG = ProductCatalog.load()


def file_search_products(keyword: str, language: str = "en") -> list[dict[str, Any]]:
    """Backwards-compatible function wrapper that supports language parameter."""

    return _DEFAULT_CATALOG.search(keyword, language)
