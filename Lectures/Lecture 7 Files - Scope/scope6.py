def outer():
    x = 5
    def inner():
        print(x)
    inner()

outer()
