# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot import handle_user_query

# Test multi-word and article variations
queries = [
    ("Do you have electric toothbrush?", "English - Electric Toothbrush"),
    ("электрическата четка", "Bulgarian - Electric Toothbrush (with article)"),
    ("Do you have a hair dryer?", "English - Hair Dryer"),
    ("електрическата сушилня", "Bulgarian - Electric Dryer (with article)"),
    ("Can I get a dryer?", "English - Dryer"),
    ("Имате ли сушилня?", "Bulgarian - Dryer"),
]

print("Multi-Word & Article Test\n" + "="*60 + "\n")
for q, label in queries:
    resp = handle_user_query(q)
    print(f"{label}")
    print(f"Q: {q}")
    print(f"A: {resp}\n")
