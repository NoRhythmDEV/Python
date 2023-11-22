#index operator [] = gives access to a sqeuence's element (str,list,tuples)

name = "max MUSTERMANN!"

#indexes the first letter of the variable "name" and checks if its lower case
if(name[0].islower()):
    #if its lower case it will be cpitalized
    name = name.capitalize()

print(name)


first_name = name[0 :3].upper()
last_name = name[4:14].lower()
last_char = name[-1]
print(first_name)
print(last_name)
print(last_char)
