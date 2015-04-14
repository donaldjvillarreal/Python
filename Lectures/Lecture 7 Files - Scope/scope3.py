x = 1

def scope_function():
    x += 1 #Fails
    print(x)
    
scope_function()