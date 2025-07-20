"""
Read and Print All Employee Names from data.json file.
"""
import json

try:
    with open("data.json", "r") as f:
        data = json.load(f) # Load JSON as Python dictionary
        for emp in data["employees"]:
            print(emp["name"])
except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON format")
