# *args = parameter that will pack all arguemnts into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*addition):
    sum = 0
    # addition = list(addition) <--- can be cast from a tuple to a list, so it mutible
    # addition[5] = 0 #changed the value in the tuple/list at index 5 to 0 (in this case the 6)

    for i in addition:
        sum += i
    return sum

print(add(1,2,3,4,5,6))