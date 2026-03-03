# pyhton writting files(.txt, .csv , .json)

# txt_data = "I like Pizza!"

Employees = ["Rohit", "sam", "john", "doe"]

file_path =  "C:/Users/rohit/Desktop/output.txt"
try:
    with open(file_path, "a") as file:
        for employye in Employees:
            file.write(employye + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")