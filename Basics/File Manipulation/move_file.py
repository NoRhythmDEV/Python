import os

source = "Files\\test.txt"
destination = "Files\\copydir\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file with this name")
    else:
        os.replace(source,destination)
        print(source+" was moved!")

except FileNotFoundError:
    print(source +" was not found")
