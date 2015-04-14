def outer():
    x = 1
    return

def inner():
    print(x) #Fails  

my_function = inner
my_function()