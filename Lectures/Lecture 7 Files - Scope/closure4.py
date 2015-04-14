def outer(x):
    def inner():
        print(x)
    return inner
    
func1 = outer(1)
func2 = outer(2)

func1()
func2()