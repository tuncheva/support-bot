# -*- coding: utf-8 -*-
import json
with open('data/products.json', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    name_lower = p.get('name', '').lower()
    if 'toothbrush' in name_lower or 'dryer' in name_lower:
        print(f"EN: {p['name']}")
        print(f"BG: {p['name_bg']}\n")
