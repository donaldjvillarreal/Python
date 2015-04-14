class A:
    pass

a = A()
b = a
b.x = 1
c = a
a = A()
a.x = 2

print(a.x)
print(b.x)
print(c.x)
