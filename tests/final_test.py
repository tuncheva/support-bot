# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')

from support_bot import handle_user_query

# Final comprehensive test
queries = [
    ("Do you have a smartwatch?", "English - SmartWatch"),
    ("Имате ли умен часовник?", "Bulgarian - SmartWatch"),
    ("Can I get an electric dryer?", "English - Electric Dryer"),
    ("электрическата сушилня", "Bulgarian - Electric Dryer (with article)"),
    ("четката за зъби", "Bulgarian - Toothbrush (with article)"),
    ("Do you sell mechanical keyboards?", "English - Mechanical Keyboard"),
]

print("Final Test Suite\n" + "="*70 + "\n")
for q, label in queries:
    resp = handle_user_query(q)
    resp_short = resp[:110] + "..." if len(resp) > 110 else resp
    print(f"{label}")
    print(f"  Q: {q}")
    print(f"  A: {resp_short}\n")
