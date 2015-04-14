def logger(func):
    def inner(*args, **kwargs):
        print("The arguments for", func.__name__, "are:", args)
        print("The keyword arguments for", func.__name__, "are:", kwargs)
        ret = func(*args, **kwargs)
        print("The value returned from", func.__name__, "is:", ret)
        return ret
    return inner

@logger
def add(x, y):
    return x + y
    
print(add(2, 3))
print("==============")

@logger
def add_three(a, b, c):
    sum1 = add(a, b)
    sum2 = add(sum1, c)
    return sum2
    
print(add_three(b=4, a=5, c=6))