def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()

outer()
