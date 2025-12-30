# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot.services.product_catalog import ProductCatalog

catalog = ProductCatalog.load()

# Test normalization
test_words = ['электрическата', 'электрическа', 'четка', 'сушилня']

print("Normalization test:")
for word in test_words:
    normalized = catalog._normalize_bulgarian(word)
    print(f"  '{word}' → '{normalized}'")

# Test search with debug
print("\n\nSearch debug - 'сушилня':")
keyword = 'сушилня'
name_field = 'name_bg'
desc_field = 'description_bg'

for p in catalog.products[:10]:
    name_text = str(p.get(name_field, "")).lower()
    desc_text = str(p.get(desc_field, "")).lower()
    
    if 'сушилн' in name_text or 'сушилн' in desc_text or 'четк' in name_text or 'четк' in desc_text:
        print(f"\n{p['name_bg']}")
        print(f"  Name: {name_text}")
        print(f"  Desc: {desc_text[:100]}")
