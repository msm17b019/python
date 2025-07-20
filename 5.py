"""
Find keys with max value in a dictionary.
"""

def key_max(dict):
    final = []
    max_value = max(dict.values())

    for key in dict:
        if dict[key] == max_value:
            final.append(key)

    return final

print(key_max({"a": 34, "b": 23, "c": 56, "d": 3, "e": 35, "f": 56}))
