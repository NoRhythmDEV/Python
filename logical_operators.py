# logical op (and, or, not)


temp = float(input("What is the Temperature outside?: "))

if temp >=0 and temp <=30:
    print("The Temperature outside is fine \ngo outside")
elif temp <0 or temp >30:
    print("The Temperature outside is bad \nstay inside")