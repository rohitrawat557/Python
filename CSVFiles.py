import csv

employees = [ 
    ["Name", "Age", "Department"],
    ["Spongebob", 30, "cook"],
    ["Rohit", 20, "IT"],
    ["Sandy", 27, "Scientist"]
]

file_path =  "C:/Users/rohit/Desktop/output.csv"
try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")