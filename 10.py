"""
Find the Most Frequent Word.

In a large file notes.txt, find and print the most frequently occurring word.

Ignore case and punctuation like . , ! ?.
"""
import string
from collections import Counter
try:
    with open("notes.txt", "r") as f:
        text = f.read()
        text = text.lower()
        for punc in string.punctuation:
            text = text.replace(punc, "")
        words = text.split()
        freq = Counter(words)
        most_common = freq.most_common(1)[0]
        print(f"The most frequent word is {most_common[0]} (Count is {most_common[1]})")
except FileNotFoundError:
    print("File not found!")
