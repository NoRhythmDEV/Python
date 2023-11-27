#loop inside loop. Wow who would've thought

#takes input of rows
rows = int(input("How many Rows? "))
#takes input of columns
columns = int(input("How many Columns? "))
#takes input what symbol to use
symbol = input("Enter a Symbol to use: ")

#outer loop
for i in range(rows):
    #inner loop
    for j in range(columns):
        #print the symbol, since the print statement each time it is call goes into a new line, we add end="". This part is in the inner loop and will print the chooses symbol
        print(symbol,end="")
    #this is in the outer loop and the print() will go into a new line each time the outer loop is executed, so it creates a new "row"
    print()
