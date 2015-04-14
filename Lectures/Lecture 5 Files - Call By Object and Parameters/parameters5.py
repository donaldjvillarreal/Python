def print_three_with_defaults(x=1, y=2, z=3):
    print(x)
    print(y)
    print(z)
    print("")
    
my_dict = {'z':5, 'x':4}

print_three_with_defaults(**my_dict)