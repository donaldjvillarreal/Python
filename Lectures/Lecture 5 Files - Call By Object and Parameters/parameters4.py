def print_any_amount(*args):
    for arg in args:
        print(arg)
    print("")
    
my_list = [1,2,3,4,5]

print_any_amount(*my_list)
print_any_amount(1,2,3,4,7)
print_any_amount(my_list)