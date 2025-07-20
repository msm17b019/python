"""
Count Words and Lines

Count:
	•	total number of lines
	•	total number of words
	•	total number of characters in the file data.txt.
"""

try:
    with open("data.txt", "r") as f:
        lines = 0
        words = 0
        chars = 0
        for line in f:
            lines += 1
            chars += len(line)
            words += len(line.split())

    print(f"Number of lines is {lines}.")
    print(f"Number of words is {words}.")
    print(f"Number of characters is {chars}.")

except FileNotFoundError:
    print("File not found!")
