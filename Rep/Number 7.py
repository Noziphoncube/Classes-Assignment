class NegativeNumberError(Exception):
    pass
def CheckPositive(num):
    if num<0:
        raise NegativeNumberError("Negative Number Encountered")
    return "Number Is Positive"

try:
    num1 = int(input("Enter A Number: "))
    print(CheckPositive(num1))
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Please enter a number")
        
