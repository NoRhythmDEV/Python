#loop control

#break = breaks loops
#continue = skips iteration
#pass = does nothing (placeholder)

#break
#infinite loop
while True:
    name = input("What is your name? ")
    if name != "":
        break
print("Your name is " + name)


#continue

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")