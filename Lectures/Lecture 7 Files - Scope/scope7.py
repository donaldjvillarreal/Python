def outer():
    x = 5
    def inner():
        x += 1 #Fails
        print(x)
    inner()

outer()
