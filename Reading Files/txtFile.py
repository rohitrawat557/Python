

file_path = "C:/Users/rohit/Desktop/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file!")