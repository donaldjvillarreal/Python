def outer(x):
    def inner():
        print(x+1)
    return inner
    
func1 = outer(1)
func2 = outer(2)

func1()
func2()