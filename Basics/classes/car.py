class Car:  #naming convetion for classes is capitalized. If Class is large its better to put it in another .py and import it

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} has stopped")
