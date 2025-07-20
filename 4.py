"""
Merge two dictionaries.
"""

def merge_dict(dict1,dict2):
    final = dict1.copy()

    for key in dict2:
        final[key] = dict2[key]
    return final

print(merge_dict({"a": 1, "b":3}, {"d": 5, "b": 2}))
