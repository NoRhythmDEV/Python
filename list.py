#list used to store multiple items in a single variable


#list
food_list = ["Pizza","Sushi","Borger"]

#prints whole list
print("Prints out the whole list\n" + str(food_list) +"\n")

#prints the item in the list with the index 2, in this case Borger
print("Prints index 2 out of the list\n" + food_list[2] + "\n")

#changes the list item in the given index
food_list[2] = "Not Borger anymore\n"
print(food_list[2])

list_functions = ["Item1","Item2","Item3"]

#list_functions.append("Item4") #Adds Item to List
#list_functions.remove("Item2") #Removes Item from List
#list_functions.pop() #removes last Item in List
#list_functions.insert(0,"Item0") #Inserts Item in List at given Index
#list_functions.sort() #Will Sort list Alphabeticaly
#list_functions.clear() #clears list.. duh


for x in list_functions:
    print(x)