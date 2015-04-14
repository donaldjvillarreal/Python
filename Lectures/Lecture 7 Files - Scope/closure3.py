def outer():
    x = 1
    def inner():
        print(x)
    return
    
my_function = inner #Fails
my_function()