def func1(other_function, x):
    y = other_function(x)
    return y+1
    
def func2(x):
    return x+2
    
def func3(x):
    return x+3
    
print(func1(func2, 2))
print(func1(func3, 2))