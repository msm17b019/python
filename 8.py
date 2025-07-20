"""
Given a file log.txt, print all lines that contain the word "ERROR" (case-sensitive).
"""

try:
    with open("log.txt", "r") as f:
        for line in f:
            if "ERROR" in line:
                print(line, end="")

except FileNotFoundError:
    print("File not found!")
