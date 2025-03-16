class shape:
    def area(self):
        pass

    def calculate_rectangle(self):
        pass

class Square(shape):
    def __init__(self, side):
        self.side = side

        def area(self):
            return self.side * self.side


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

        def area(self):
            return 22/7 * self.radius * 2


class RightAngleTri(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

        def area(self):
            return self.base/2 * self.height


class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

        def calculate_rectangle(self):
            print ("area of a rectangle is " + self.length * self.width)