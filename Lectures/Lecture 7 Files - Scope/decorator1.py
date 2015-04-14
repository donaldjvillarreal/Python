def outer(func):
    def inner():
        ret = func()
        return ret + 1
    return inner
    
def my_function():
    return 2

print(my_function())
    
my_function = outer(my_function)
print(my_function())

my_function = outer(my_function)
print(my_function())