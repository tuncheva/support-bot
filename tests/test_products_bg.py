# -*- coding: utf-8 -*-
import json
import sys
sys.path.insert(0, 'src')

with open('data/products.json', encoding='utf-8') as f:
    products = json.load(f)

# Search for headphone-like products
keywords = ['слушалки', 'трака', 'часовник']

for kw in keywords:
    print(f"\nSearching for '{kw}':")
    matches = []
    for p in products:
        if kw.lower() in p.get('name_bg', '').lower() or kw.lower() in p.get('description_bg', '').lower():
            matches.append(f"  {p['name_bg']}")
    if matches:
        for m in matches[:3]:
            print(m)
    else:
        print("  No matches")
