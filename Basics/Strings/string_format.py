import math
#str.format() = optional method that gives users more control when displaying output


animal = "cow"
item = "moon"

# method 1 with concatination
print("The "+animal+" jumped over the "+ item)

#method 2 with formation function and given values {}=placeholder (format fields), first format field will fill in the first value, then the next and so on
print("The {} jumped over the {}".format(animal,item))

#method 3 same as 2 but with indexing    i=0   i=1 ....
print("The {1} jumped over the {0}".format(item,animal))

#method 4 same as 2 but with keywording   
print("The {animal} jumped over the {item}".format(item="moon",animal="cow"))

#method 5 using a variable
text = "The {} jumped over the {}"
print(text.format(animal,item))

#normal output
name = "Max Mustermann"
print("Hello, my name is {}".format(name))
#output with padding {:5} adds 100 spaces
print("Hello, my name is {:100}. Nice to meet you".format(name))
print("Hello, my name is {:<100}. Nice to meet you".format(name)) #left aligned
print("Hello, my name is {:>100}. Nice to meet you".format(name)) #right aligned
print("Hello, my name is {:^100}. Nice to meet you".format(name)) #center aligned



number_pi = math.pi
number = 1000000
print("The first 8 Digits of the Number Pi are: {:.8f}".format(number_pi))
print("Adds a Comma to every thousand point (Number without formating 1000000). With Formatting: {:,}".format(number))
print("This will change the number {}".format(number) + " to Binary {:b}".format(number))
print("This will change the number {}".format(number) + " to Octal --> {:o}".format(number))
print("This will change the number {}".format(number) + " to Hexadecimal --> {:X}".format(number)) #x for lower case or X for upper case
print("This will change the number {}".format(number) + " to scientific notation --> {:e}".format(number)) #e for lower case or E for upper case

