#type casting = convert datatype to another datatype

x = 1 #int
y = 2.0 #float
z = "3" #str

print(x)
print(y)
print(z)

print(z*3) #Will print 333 since you cant do math with str

print(int(z)*3) #cast the str to int, now it will print 9

#print("x is "+x) <--- this wont work since you can't concat non-str

print("x is "+str(x)) #this will now work since the int is cast to a str and can be concatinated