#exceptions = events detected during execution that interrupt the flow of  programm


#would throw a error if you would try to divide by 0
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print("Can't divide by 0")
    print(e)
except ValueError as e:
    print("Only input Numbers please")
except Exception as e:
    print("Something went wrong :(")