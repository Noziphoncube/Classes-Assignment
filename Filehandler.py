from abc import ABC, abstractmethod

class filehandler(ABC):
    def __init__(self, filename):
        self.filename = filename

        @abstractmethod
        def read(self):
            pass

        @abstractmethod
        def write(self, data):
            pass

class Textfilehandler(filehandler):
    def read(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print ("File " + {self.filename} + " not found")
            return None

    def write(self, data):
        with open(self.filename, 'w') as file:
                file.write(data)

class BinaryFileHandler(filehandler):
    def read(self):
        try:
            with open(self.filename, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print  ("File " + {self.filename} + " not found")
            return None

    def write(self, data):
        with open(self.filename, 'wb') as file:
                file.write(data)


