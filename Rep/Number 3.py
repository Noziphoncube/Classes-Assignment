while True:
    try:
        num=float(input("Enter A Number: "))
        print(f"You Entered {num}")
        break
    except ValueError:
        print("Please Enter A Valid Number")
