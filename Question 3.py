6class shape:
    def __init__(self,name):
        self.name=name
        print(f"Shape constructor called for {self.name}")

    def calc_area(self):
        pass

class rectangle(shape):
    def __init__(self, width, length):
        super().__init__("rectangle")
        self.width=width
        self.length=length
        
    def calc_area(self):
        super().__init__("rectangle")
        return self.width*self.length

b=float(input("Length Of Rectangle: "))
a=float(input("Width Of Rectangle: "))
rect=rectangle(a,b)
print(f"Area Of Rectangle Is {rect.calc_area()}")
