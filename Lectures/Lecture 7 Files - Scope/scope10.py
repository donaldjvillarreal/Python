x = -8

def increase():
    global x
    print(x, "is less than zero!")
    x += 1

def decrease():
    global x
    print(x, "is more than zero!")
    x -= 1
    
if x < 0:
    move_toward_zero = increase
else:
    move_toward_zero = decrease
    
while x != 0:
    move_toward_zero()
