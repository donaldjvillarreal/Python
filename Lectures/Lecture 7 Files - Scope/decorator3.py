def add_one(func):
    def inner(x):
        ret = func(x)
        return ret + 1
    return inner

@add_one  
def return_same(x):
    return x
    
print(return_same(2))
