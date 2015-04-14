class A:
    def b(self):
        print("Hello")
        
def c(self):
    print("World")
    
A.d = c

a = A()
a.b()
a.d()
