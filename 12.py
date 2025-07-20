"""
Print the names of all employees who belong to the "IT" department from data.json file.
"""

import json
try:
    with open("data.json", "r") as f:
        data = json.load(f)
        for emp in data["employees"]:
            if emp["department"] == "IT":
                print(emp["name"])
except FileNotFoundError:
    print("file not found!")
except json.JSONDecodeError:
    print("invalid json format!")
