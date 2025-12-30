# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')
from support_bot.services.product_catalog import file_search_products

results = file_search_products('интелигентни часовници', language='bg')
print(f'Smart watches search: {len(results)} results')
if results:
    for i, r in enumerate(results[:3]):
        print(f'  {i+1}. {r["name_bg"]}')