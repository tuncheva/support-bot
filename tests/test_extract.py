# -*- coding: utf-8 -*-
import re

def debug_extract(text):
    is_bulgarian = bool(re.search(r'[\u0400-\u04FF]', text))
    print(f"\nText: {text}")
    print(f"Is Bulgarian: {is_bulgarian}")
    
    common_words = {"do", "you", "sell", "have", "what", "can", "is", "it", "the", "a", "an", "or", "and", "price", "of", "for", "with", "in", "on", "at", "to", "that", "this", "about", "does", 
                  "до", "вие", "продавате", "имате", "ли", "какво", "е", "цена", "на", "какъв", "има", "по", "един", "в", "с", "от", "за", "то", "търся", "той", "тя", "то"}
    
    if is_bulgarian:
        words = re.findall(r"[\u0400-\u04FF]{3,}", text, re.IGNORECASE)
        print(f"  All words: {words}")
        filtered = [w for w in words if w.lower() not in common_words]
        print(f"  Filtered: {filtered}")
        sorted_words = sorted(set(words), key=lambda w: len(w), reverse=True)
        print(f"  Sorted by length: {sorted_words}")
        for word in sorted_words:
            if word.lower() not in common_words:
                print(f"  Selected: {word}")
                break
    else:
        words = re.findall(r"\b[a-z]{3,}\b", text.lower())
        print(f"  All words: {words}")
        filtered = [w for w in words if w not in common_words]
        print(f"  Filtered: {filtered}")
        sorted_words = sorted(set(words), key=len, reverse=True)
        print(f"  Sorted by length: {sorted_words}")
        for word in sorted_words:
            if word not in common_words:
                print(f"  Selected: {word}")
                break

debug_extract("Имате ли слушалки?")
debug_extract("Цена на интелигентния часовник")
debug_extract("What about headphones?")
