#tuple = collections which is ordered and unchangeable
#         used to group together related data
#         similar to Lists but used () instead of []

student = ("Max",21,"male")

#prints the count how often the given value is in the tuple
print(student.count(21))
#prints the index where the given value is located at
print(student.index("Max"))

#Will Print all the Values in a tuple
for x in student:
    print(x)

#prints only if the asked value is given in the tuple
if "Max" in student:
    print("Max is here!")