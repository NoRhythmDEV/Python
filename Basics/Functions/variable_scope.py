#scope = the region that a variable is recognized
# a variable is only available from inside the region it is created
# a gloabl and locally scoped version of a variable can be created

name = "Max Mustermann (Global)" #global scope since it isnt created inside a function.

#The same variable name can be used since the on is global and the one inside the function is local

def display_name():
    name = "Max Mustermann (Local)" #variable scope = local, only available inside the function since it is created in there
    print(name)


display_name()
print(name) 


#local variable will be used before global variables