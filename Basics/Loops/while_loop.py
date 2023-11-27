#while loop. Loops through the code aslong as the condition is true

#this will create a infite loop
# while True:
#     print("help im stuck")

#empty str 
name = ""

#condition checks if the lenght of the name variable is 0, will repeat the code aslong as the user doesnt input anything
while len(name) == 0:
   name = input("Please enter your Name: ")


print("Hello " + name)