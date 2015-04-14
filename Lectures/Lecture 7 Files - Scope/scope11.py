def outer():
    def inner():
        print("Running inner function")
    return inner
    
my_function = outer()
my_function()
