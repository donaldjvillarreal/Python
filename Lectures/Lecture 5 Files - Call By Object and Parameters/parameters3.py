def print_three(x, y, z):
    print(x)
    print(y)
    print(z)
    print("")
    
my_list = [1, 2, 3]

print_three(my_list[0], my_list[1], my_list[2])

print_three(*my_list)

my_other_list = [2, 3]

print_three(1, *my_other_list)
