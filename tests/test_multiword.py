# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot.services.product_catalog import file_search_products

# Test multi-word and article variations
tests = [
    ("електрическата сушилня", "bg", "Should match Dryer (both words)"),
    ("сушилня", "bg", "Should match Dryer"),
    ("електрическа четка", "bg", "Should match Electric Toothbrush (both words)"),
    ("електрическата четка", "bg", "Should match Electric Toothbrush (with article)"),
    ("четка за зъби", "bg", "Should match Electric Toothbrush"),
    ("hair dryer", "en", "Should match Hair Dryer"),
]

for query, lang, description in tests:
    results = file_search_products(query, language=lang)
    print(f"\n{description}")
    print(f"Query: '{query}' ({lang})")
    if results:
        for i, r in enumerate(results[:2]):
            field = 'name_bg' if lang == 'bg' else 'name'
            print(f"  {i+1}. {r[field]}")
    else:
        print("  No matches")
