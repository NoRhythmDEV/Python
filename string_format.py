#str.format() = optional method that gives users more control when displaying output


animal = "cow"
item = "moon"

# method 1 with concatination
print("The "+animal+" jumped over the "+ item)
#method 2 with formation function and given values {}=placeholder (format fields), first format field will fill in the first value, then the next and so on
print("The {} jumped over the {}".format(animal,item))
#method 3 same as 2 but with indexing    i=0   i=1 ....
print("The {1} jumped over the {0}".format(item,animal))