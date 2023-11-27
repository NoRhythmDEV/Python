#Python Object Oriented Programming (OOP)

#import class

from car import Car

car_model = int(input("What car would you like to choose 1 or 2? "))

if car_model == 1:
    car_1 = Car("Chevy","Corvett",2021,"Black")
    print(car_1.make)
    print(car_1.model)
    print(car_1.year)
    print(car_1.color)
    car_1.drive()
    car_1.stop()

elif car_model == 2:
    car_2 = Car("Ford","Mustang",2022,"Blue")
    print(car_2.make)
    print(car_2.model)
    print(car_2.year)
    print(car_2.color)
    car_2.drive()
    car_2.stop()
