def outer():
    def inner(x):
        print(x)  
    inner(3)
    inner(4)

outer()

inner(5) #Fails