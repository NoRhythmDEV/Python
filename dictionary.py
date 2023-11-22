#dictionary = a changeable, unordered collection of unique key:value pairs
#             fast search, because of hashing

capitals = {"Germany":"Berlin",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"
            }

#print(capitals)

# user_input = input("What Capital do u want to know? ")
# user_input_capitalized = user_input.capitalize()
# print(capitals.get(user_input_capitalized))

#update function with user input
input_country = str(input("Which Country do u want to add? "))
input_capital = str(input("Now add the Capital of "+input_country+": "))

capitals.update({input_country:input_capital})

print("\nCountry <-> Capital\n")
for key,value in capitals.items():
    print(key, "<->", value)
