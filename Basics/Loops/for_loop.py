import time

#for loop will repeat code aslong as the condition is true
#for loop = limited
#while loop = unlimited

#for loop that will be repeat 3 times (range(3))
for i in range(3):
    print(i) #output 0 1 2 
print("end of loop 1")
#since computers start at 0 we can fix it in 2 ways 
#print(i+1)
for i in range(3):
    print(i+1) #output 1 2 3
print("end of loop 2")
#or for i in range(3+1):
for i in range(3+1): 
    print(i) #output 0 1 2 3
print("end of loop 3")

#in a range of numbers i.e. 3,9 (3-9) the first number (3) is inclusive so it will be printed in the output, the last number is exclusive so it wont be printed
#if you want the last number in the range to be printed, add a +1 to it ---> for i in range(3,9+1)
for i in range(3,9+1):
    print(i)
print("end of loop 4")

#the third arg is the step so it will print all 10 steps
for i in range(50,100+1,10):
    print(i)
print("end of loop 5")

#this will print out each lette in the string
for i in "test":
    print(i)
print("end of loop 6")

#for loop with timer
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("you waited 10 seconds. Congrats")