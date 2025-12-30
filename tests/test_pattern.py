# -*- coding: utf-8 -*-
import re

text = "Цена на интелигентния часовник"

# Test the pattern
pattern = r"(?:sell|have|price\s+of|about|търся|имате|цена\s+на)\s+(?:a\s+)?(?:the\s+)?([^\s?!.,]+)"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print(f"Pattern matched: '{match.group(1)}'")
else:
    print("No pattern match")
