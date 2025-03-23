def classify_number(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return 'zero'
    return

while True:
    inp=input("Enter A Number: ")
    if inp.isdigit() or (inp.startswith("-") and inp[1:]):
        num=int(inp)
        print("The Number Is "+ classify_number(num))
        break
    else:
        print("Please Enter A Valid Integer")
