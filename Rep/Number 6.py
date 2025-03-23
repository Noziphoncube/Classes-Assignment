def divide_numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "Can Not Divide By Zero"
    except TypeError:
        return "Invalid Input. Please Put In Numbers"
    return
a=float(input("Enter Numerator: "))
b=float(input("Enter Denominator: "))
print(divide_numbers(a,b))
