# -*- coding: utf-8 -*-
import json
with open('data/products.json', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    name_bg = p.get('name_bg', '')
    if 'watch' in p['name'].lower() or 'час' in name_bg.lower():
        print(f"EN: {p['name']}")
        print(f"BG: {name_bg}")
        print()
