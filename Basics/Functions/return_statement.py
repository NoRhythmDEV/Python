#return statement = functions send python values/objects back to the caller.
#                   these values/objects are know as the functions return value



def multiply(number1, number2):
    return float(number1) + float(number2)

# x = multiply(6*9)
# print(x)


# simply calc


def add(number1, number2):
    return float(number1) + float(number2)

def sub(number1, number2):
    return float(number1) - float(number2)

def div(number1, number2):
    if float(number2) != 0:
        return float(number1) / float(number2)
    else:
        return "Error: Division by zero"

number1 = input("First Number: ")
number2 = input("Second Number: ")
operator = input("Choose your operator\n+\n-\n*\n/\n")

if operator == "*":
    print("Result: " + str(multiply(number1, number2)))
elif operator == "-":
    print("Result: " + str(sub(number1, number2)))
elif operator == "+":
    print("Result: " + str(add(number1, number2)))
elif operator == "/":
    print("Result: " + str(div(number1, number2)))
else:
    print("Invalid operator")
