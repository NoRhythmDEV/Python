import os
import shutil

try:
    path = "Files\\test.txt"
    os.remove(path) #removes files
    os.rmdir(path) #removes empty dir
    shutil.rmtree(path) #removes dir regardless if its empty or not
except FileNotFoundError as e:
    print(path + " Not Found")
except PermissionError as e:
    print("You do not have permission")
else:
    print(path +" Deleted")