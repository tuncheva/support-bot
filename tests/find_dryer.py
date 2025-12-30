# -*- coding: utf-8 -*-
import json
with open('data/products.json', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    if 'Сушил' in p['name_bg'] or 'Hair Dry' in p['name']:
        print(f"EN: {p['name']}")
        print(f"BG: {p['name_bg']}")
        print()
