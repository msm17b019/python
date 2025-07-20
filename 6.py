"""
Group words by anagram.

Anagrams: Two words are anagrams if they contain the same letters in a different order.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
"""

def group_anagrams(words):
    anagram_groups = {}

    for word in words:
        key = tuple(sorted(word))

        if key not in anagram_groups:
            anagram_groups[key] = []

        anagram_groups[key].append(word)

    return list(anagram_groups.values())

print(group_anagrams(["eat", "ate", "ant", "bat", "nat", "rat", "tae"]))
