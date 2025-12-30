# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot import handle_user_query

# Comprehensive test suite
queries = [
    # English - basic
    ("Do you sell laptops?", "English - Laptop"),
    ("What headphones do you have?", "English - Headphones"),
    ("I want a keyboard", "English - Keyboard"),
    ("Can I get a dryer?", "English - Dryer"),
    
    # Bulgarian - basic
    ("Търся лаптоп", "Bulgarian - Laptop"),
    ("Имате ли слушалки?", "Bulgarian - Headphones"),
    ("Цена на клавиатура", "Bulgarian - Keyboard"),
    
    # Bulgarian - multi-word
    ("Търся електрическата четка", "Bulgarian - Electric Toothbrush"),
    ("электрическата сушилня", "Bulgarian - Electric Dryer"),
    ("Имате ли интелигентни часовници?", "Bulgarian - Smart Watches"),
    
    # Bulgarian - with articles/endings
    ("четката за зъби", "Bulgarian - Toothbrush (with article)"),
    ("клавиатурата", "Bulgarian - Keyboard (with article)"),
]

print("Comprehensive Test Suite\n" + "="*70 + "\n")
for q, label in queries:
    resp = handle_user_query(q)
    # Truncate long responses
    resp_short = resp[:100] + "..." if len(resp) > 100 else resp
    print(f"{label}")
    print(f"  Q: {q}")
    print(f"  A: {resp_short}\n")
