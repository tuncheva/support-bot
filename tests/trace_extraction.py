# -*- coding: utf-8 -*-
import sys
import re
sys.path.insert(0, 'src')

# Test keyword extraction for Bulgarian queries
test_queries = [
    "Имате ли сушилня?",
    "электрическата сушилня",
    "электрическата четка"
]

common_words = {"до", "вие", "продавате", "имате", "ли", "какво", "е", "цена", "на", "какъв", "има", "по", "а", "един", "в", "с", "от", "за", "то", "търся"}

for text in test_queries:
    print(f"\n\nQuery: '{text}'")
    
    is_bulgarian = bool(re.search(r'[\u0400-\u04FF]', text))
    language = "bg" if is_bulgarian else "en"
    
    # Try patterns first
    patterns = [
        r"(?:sell|have|price\s+of|about|търся|имате|цена\s+на)\s+(?:a\s+)?(?:the\s+)?(\w+)",
        r"(?:treadmill|skateboard|router|chair|lamp|headphone|camera|monitor|speaker|keyboard|mouse|phone|tablet|watch|charger|cable)",
    ]
    
    prod_term = None
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            prod_term = match.group(1) if match.lastindex else match.group(0)
            print(f"  Pattern matched: '{prod_term}'")
            break
    
    if not prod_term:
        print(f"  No pattern matched, extracting longest word")
        if language == 'bg':
            words = re.findall(r"[\u0400-\u04FF]{3,}", text, re.IGNORECASE)
        else:
            words = re.findall(r"\b[a-z]{3,}\b", text.lower())
        print(f"  Found words: {words}")
        
        for word in sorted(words, key=len, reverse=True):
            if word.lower() not in common_words:
                prod_term = word
                print(f"  Selected: '{prod_term}'")
                break
    
    if prod_term:
        print(f"  Final search term: '{prod_term}'")
