import random #import lib

#will generate a random number with the range 1-10
x = random.randint(1,10)
print(x)

y = random.random()
print(y)

#random choice from a list
myList = ["Rock","Paper","Scissors"]
z = random.choice(myList)
print(z)


#shuffle a list
cards = [1,2,3,4,5,6,7,8,9,"Jack","Queen","King","Ace"]
random.shuffle(cards)
print(cards)