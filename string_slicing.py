name = "Max Mustermann" #string with full name

substring_firstname = name[0:3:1] #takes in variable in this case a string and a index [start:stop:step], computers start at 0 so M is 0 and x is 3. This is because the Starting Point is 
                                  #inluding and the stopping Point is excluding. The step is with which value it increases. In this case its 1 and the output is -> Max if it would increase by 2 the
                                  #output would be -> Mx

substring_lastname = name[4::1] #Spaces will be ignored.
                                #Aslong as you have a starting point and the colon (:) it will count from the starting point until the end
                                #Step is optional. Default is 1

print(substring_firstname)
print(substring_lastname)