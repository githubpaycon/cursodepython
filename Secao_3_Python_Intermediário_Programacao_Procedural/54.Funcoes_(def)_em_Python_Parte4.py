def func1():
    var1 = 10
    return var1


def func2(arg):
    arg = bool(arg)
    print(arg)


func1var = func1()
func2(func1var)