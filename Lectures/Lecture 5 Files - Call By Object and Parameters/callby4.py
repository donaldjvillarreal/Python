def f1(x):
    x[0][0] = "banana"
    x[1] = "grape"

def f2(x):
    x[0] = "lemon"
    
def f3(x):
    x = "lime"

z = ["orange", "apple"]
y = [z, "pear"]

f1(y)
print(y)

f2(y)
print(y)

f3(y)
print(y)