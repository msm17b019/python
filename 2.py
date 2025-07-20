"""
Reverse a list without using built-in reverse

Example:
a = [1,4,5,3,6,2]
output = [2,6,3,5,4,1]
"""

def rev_list(lst):
    final = []
    for index,item in enumerate(lst):
        final.append(lst[-(index+1)])
    return final

print(rev_list([2,4,6,2,1,8,5]))
print(rev_list([6,4,8,3,5,2,5,9]))
print(rev_list([1,4,5,3,6,2]))
