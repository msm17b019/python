"""
You have a file named data.txt. Write a Python script to read and print all lines from the file.
"""

with open("./data.txt","r") as f:
    for line in f:
        print(line, end="")
