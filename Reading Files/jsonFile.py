import json

file_path = "C:/Users/rohit/Desktop/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file!")