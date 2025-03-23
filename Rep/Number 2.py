def calculate_average(*args):
    if not args:
        return 0
    avg = sum(args)/len(args)
    print(avg)
    return
calculate_average(5,3,16)
