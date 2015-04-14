class A:
    def __init__(self):
        self.x = 2
        
class B(A):
    pass
    
b = B()
print(b.x)