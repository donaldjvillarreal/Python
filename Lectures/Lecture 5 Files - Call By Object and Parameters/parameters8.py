def print_two_and_any_amount(x, y, *args):
    print(x)
    print(y)
    for arg in args:
        print(arg)
    print("")
    
print_two_and_any_amount(1,2)
print_two_and_any_amount(1,2,3,4,5,6,7)
