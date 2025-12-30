# -*- coding: utf-8 -*-
import sys
import re
sys.path.insert(0, 'src')

from support_bot.services.product_catalog import ProductCatalog

catalog = ProductCatalog.load()

# Manually test search for "сушилня"
keyword = 'сушилня'
language = 'bg'
name_field = 'name_bg'
desc_field = 'description_bg'

keywords = keyword.split()
normalized_keywords = [catalog._normalize_bulgarian(kw) for kw in keywords]

print(f"Searching for: '{keyword}'")
print(f"Normalized: {normalized_keywords}")

# Find "Dryer" product
dryer_product = None
for p in catalog.products:
    if p.get('name_bg') == 'Сушилня':
        dryer_product = p
        break

if dryer_product:
    print(f"\nFound Dryer product: {dryer_product['name_bg']}")
    name_text = str(dryer_product.get(name_field, "")).lower()
    desc_text = str(dryer_product.get(desc_field, "")).lower()
    print(f"Name text: '{name_text}'")
    print(f"Desc text: '{desc_text[:80]}'")
    
    # Check normalization
    name_words = re.findall(r'[\u0400-\u04FF]+', name_text)
    desc_words = re.findall(r'[\u0400-\u04FF]+', desc_text)
    print(f"Name words: {name_words}")
    print(f"Desc words (first 5): {desc_words[:5]}")
    
    normalized_product_text = " ".join(
        [catalog._normalize_bulgarian(w) for w in name_words + desc_words]
    )
    print(f"Normalized product text: '{normalized_product_text}'")
    
    # Check if search keyword is in normalized text
    for norm_kw in normalized_keywords:
        found = norm_kw in normalized_product_text
        print(f"\nSearching for normalized keyword '{norm_kw}': {found}")
