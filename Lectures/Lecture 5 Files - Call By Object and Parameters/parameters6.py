def print_three(x, y, z):
    print(x)
    print(y)
    print(z)
    print("")
    
my_dict = {'y':2, 'z':3, 'x':1}

print_three(**my_dict)

my_dict = {'z':3, 'y':2}

print_three(1, **my_dict)