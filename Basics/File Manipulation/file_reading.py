try:
    with open("Files\\test.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found")
    print(e)
