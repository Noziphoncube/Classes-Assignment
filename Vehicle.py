class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.driven = 0

    def drive(self, kilometers):
        self.driven += kilometers

    def describe_vehicle(self):
        print("Vehicle is " + {self.brand} + " make " + {self.model} + " from " + {self.year})

class Car(vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def describe_vehicle(self):
        super().describe_vehicle()
        print("It's a car that has " + {self.doors} + " doors")

class bike(vehicle):
    def __init__(self, brand, model, year, enginesize):
        super().__init__(brand, model, year)
        self.enginesize = enginesize

    def describe_vehicle(self):
        super().describe_vehicle()
        print("It's a bike that has " + {self.enginesize} + " sized engine")
