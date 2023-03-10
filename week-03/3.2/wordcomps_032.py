#!/usr/bin/env python3


import sys

def allvowels(w):
    return "a" in w and "e" in w and "i" in w and "o" in w and "u" in w


lines = [line.strip() for line in sys.stdin]

words_allvowels = [w for w in lines if allvowels(w.lower())]
print(f"Shortest word containing all vowels: {min(words_allvowels, key=len)}")

words_iary = [w for w in lines if w.lower().endswith("iary")]
print(f"Words ending in iary: {len(words_iary)}")

most_ees = max([w.lower().count('e') for w in lines])

words_most_ees = [w for w in lines if w.lower().count("e") == most_ees]
print(f"Words with most e's: {words_most_ees}")