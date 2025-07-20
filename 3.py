"""
Count the frequency of each item in a list
"""

def count_item(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(count_item([2,4,3,5,3,5,2,3,1,4,2,1]))
