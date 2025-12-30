# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot.services.product_catalog import file_search_products

# Test search
keywords = [
    ('слушалки', 'bg'),
    ('трака', 'bg'),
    ('часовник', 'bg'),
    ('интелигентния', 'bg')
]

for kw, lang in keywords:
    results = file_search_products(kw, language=lang)
    print(f"\n'{kw}' ({lang}): {len(results)} matches")
    if results:
        print(f"  → {results[0]['name_bg']}")
