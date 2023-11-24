import os

path = "C:\\Users\jstahl\\Desktop\\Projekte\\Python\Files\\test.txt"

if os.path.exists(path):    
    print("This Location exists.")
    if os.path.isfile(path):
        print("It's a File")
    elif os.path.isdir():
        print("It's a Dir")
else:
    print("This location doesnt exist")