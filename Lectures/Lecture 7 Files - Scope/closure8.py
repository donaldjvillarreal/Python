def make_counter():
    count = 1
    def counter():
        nonlocal count
        print(count)
        count += 1
    return counter
    
c1 = make_counter()
c2 = make_counter()

c1()
c1()
c1()
c2()
c1()
c2()