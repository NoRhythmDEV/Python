#if statement = a block of code that will only execute if the condition is true

age = int(input("How old are you?: "))

#condition
if age >= 100:
    #codeblock that gets executed if condition is true
    print("you are old af")
elif age >= 18:
    print("You are 18 or older")
else:
    print("you are under 18")


