def outer():
    x = 1
    def inner():
        print(x)
    return inner
    
my_function = outer()
my_function()