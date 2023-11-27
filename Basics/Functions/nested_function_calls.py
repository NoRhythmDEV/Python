#nested funcion call = function call inside other function call
# innermost function calls are resolved first
# returned value is used for the next out function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

#this does the same as the above

print(round(abs(float(input("Enter a whole positive number: ")))))