# -*- coding: utf-8 -*-

# Check character codes
words = ['Сушилня', 'сушилня', 'Сешоар', 'сешоар']

for word in words:
    print(f"\n'{word}':")
    for ch in word:
        print(f"  {ch} = U+{ord(ch):04X}")
