def add(x, y):
    return x + y
    
def sub(x, y):
    return x - y
    
def apply(func, a, b):
    return func(a, b)
    
print(apply(add, 5, 2))
print(apply(sub, 5, 2))