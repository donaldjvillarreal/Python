def outer(x):
    def inner():
        x += 1 #Fails
        print(x)
    return inner
    
func1 = outer(1)
func2 = outer(2)

func1()
func2()