def scope_function():
    x = "This is a local variable"
    print(x)
    
scope_function()
print(x) #Fails