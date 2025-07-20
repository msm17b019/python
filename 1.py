"""
Remove duplicates from lists.
"""

def remove_dup_list(list_of_items):
    seen = set()
    final = []
    for item in list_of_items:
        if item not in seen:
            final.append(item)
            seen.add(item)

    return final

print(remove_dup_list([2,3,4,1,4,3,4,2,3]))
print(remove_dup_list(["a","v","c","s","a","b","c","s","a"]))
print(remove_dup_list([2,3,4,1,4,3,4,2,3,"a","a","b","a"]))
