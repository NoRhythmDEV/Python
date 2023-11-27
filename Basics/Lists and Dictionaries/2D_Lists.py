#2D Lists = a list of lists

drinks = [
    "coffe",
    "water",
    "cola"
]

dinner = [
    "pizza",
    "borger",
    "Sushi"
]

desert = [
    "cake",
    "ice cream"
]

#list that takes in other lists
food = [drinks,dinner,desert]

# #will print the lists in the food list
for x in food:
    print(x)

#will print the items in the list of the list at index 2
for y in food[2]:
    print(y)