def outer(func):
    def inner():
        ret = func()
        return ret + 1
    return inner

@outer
def my_function():
    return 2
    
print(my_function())