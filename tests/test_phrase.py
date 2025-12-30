# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot.services.product_catalog import file_search_products

results = file_search_products('интелигентния часовник', language='bg')
print(f"Results: {len(results)}")
if results:
    print(f"  → {results[0]['name_bg']}")

results2 = file_search_products('часовник', language='bg')
print(f"\nJust 'часовник': {len(results2)}")
if results2:
    print(f"  → {results2[0]['name_bg']}")
