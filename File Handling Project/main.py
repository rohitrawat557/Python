from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.glob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to create : ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as f:
                data = input("Enter the data you want to write in the file : ")
                f.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("file already exists")
    except Exception as e:
        print(f"an error occured as : {e}")
    
def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to read :")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as f:
                data = f.read()
                print(data)

            print("Readed Successfully")
        else:
            print("file does not exist")
    except Exception as e:
        print(f"an error occured as : {e}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file : ")
            print("press 2 for overwriting the data of the file : ")
            print("press 3 for appending the data of the file : ")

            res = int(input("Enter your response : "))

            if res == 1:
                name2 = input("Enter the new name of the file : ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, "w") as f:
                    data = input("Enter the data you want to write this will overwrite the exsiting data : ")
                    f.write(data)
            
            if res == 3: 
                with open(p, "a") as f:
                    data = input("Enter the data you want to append : ")
                    f.write(" " +data)

    except Exception as e:
        print(f"an error occured as : {e}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete : ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("file deleted successfully")

        else:
            print("no such file exists")

    except Exception as e:
        print(f"an error occured as : {e}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Enter your choice : "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()