import math

pi = math.pi
neg_pi = -math.pi

list = [3,1,6,23,14,4.5]

#rounding
print(round(pi)) #rounds to the nearest full int (built in)
print(math.ceil(pi)) #rounds up to nearest int (math module)
print(math.floor(pi)) #rounds down to nearest int(math module)

print(abs(neg_pi)) #absolute value -> The absolute value is the distance of a number from zero on the number line, regardless of its sign
print(pow(pi,2)) #takes 2 values, to raise a number by power in this example 2. pi^2
print(math.sqrt(pi)) #squares the input

#sorting numbers
print(max(list)) #prints highest number from input
print(min(list)) #prints lowest number from input


