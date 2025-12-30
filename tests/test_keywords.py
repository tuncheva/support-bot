# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, 'src')

# Test keyword extraction
test_queries = [
    "Имате ли слушалки?",
    "Търся трака за бягане",
    "Цена на интелигентния часовник"
]

common_words = {"до", "вие", "продавате", "имате", "ли", "какво", "е", "цена", "на", "какъв", "има", "по", "а", "един", "в", "с", "от", "за", "то", "търся"}

for q in test_queries:
    print(f"\nQuery: {q}")
    words = re.findall(r"[\u0400-\u04FF]{3,}", q, re.IGNORECASE)
    print(f"  All words: {words}")
    print(f"  Filtered: {[w for w in words if w.lower() not in common_words]}")
