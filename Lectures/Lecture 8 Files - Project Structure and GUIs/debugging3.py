def third(x, y):
    return x + y
    
def second(u, v):
    return third(u, v)
    
def first(a, b):
    return second(a, b)

def another_function(a, b):
    return third(a, b)

x = another_function(4, 5)
y = first(4, 'g')

print(x)
print(y)