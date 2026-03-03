import os
file_path = "C:/Users/rohit/Desktop/test"

if os.path.exists(file_path):
    print(f"The loaction '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does not exist")