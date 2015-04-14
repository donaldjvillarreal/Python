def another_function(**kwargs):
    for key, value in kwargs.items():
        print("The key %s contains the number %d" % (key, value))
    if 'x' in kwargs and 'y' in kwargs:
        print("The sum of x and y is %d" % (kwargs['x']+kwargs['y']))
    print("")
        
another_function(z=5, y=9, x=10)
        
my_dict = {'x':4, 'y':5, 'z':6}
another_function(**my_dict)

my_dict = {'apple':7, 'banana':8}
another_function(**my_dict)
