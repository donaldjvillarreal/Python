class A:
    pass
    
a = A()
a.x = 1
b = a
del a
print(b.x)
