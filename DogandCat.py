class dog:
    def make_sound(self):
        return "bark"

class cat:
    def make_sound(self):
        return "meow"

def process_sound(animal):
    sound = animal.make_sound()
    print ("The animal says " + {sound})

