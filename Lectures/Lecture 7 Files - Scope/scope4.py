x = 1

def scope_function():
    global x
    x += 1
    print(x)
    
scope_function()