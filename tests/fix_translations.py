# -*- coding: utf-8 -*-
import json

# Load products
with open('data/products.json', encoding='utf-8', mode='r') as f:
    products = json.load(f)

# Find and update products that are missing Bulgarian translations or still have English names
translations = {
    'SmartWatch Pro': 'Умен часовник Pro',
    'Smart Home Hub': 'Интелигентен домашен хъб',
    'Wireless Charger': 'Безжично зарядно',
    'USB-C Cable': 'USB-C кабел',
    'Portable Speaker': 'Портативна колона',
}

for p in products:
    if p['name_bg'] in translations:
        p['name_bg'] = translations[p['name_bg']]
        print(f"Updated: {p['name']} → {p['name_bg']}")
    elif p['name_bg'] == p['name']:  # Not translated
        # Try to find a translation
        en_name = p['name']
        if en_name in translations:
            p['name_bg'] = translations[en_name]
            print(f"Translated: {en_name} → {p['name_bg']}")

# Save
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("\nDone!")
