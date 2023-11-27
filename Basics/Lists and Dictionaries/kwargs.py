# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amunt of keyword arguments

#kwargs can be named anythings else the important thing is **
def hello(**names):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")


hello(title="",first="Max",middle="Hans",last="Mustermann")

