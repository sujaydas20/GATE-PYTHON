def fun(*args):
    return sum(args)

print(fun(2, 4, 6))









def fun(a, *args):
    print(a)
    print(args[1])

fun(10, 20, 30, 40)






def fun(**kwargs):
    print(kwargs)

fun(a=10, b=20)




def fun(**kwargs):
    return kwargs["b"] + kwargs["c"]

print(fun(a=5, b=10, c=15))





def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1, 2, x=10, y=20)









def fun(*args):
    x = 0
    for i in args:
        x += i
    return x

a = fun(1, 2)
b = fun(3, 4, 5)

print(a + b)









def fun(**kwargs):
    x = 0
    for key in kwargs:
        x += kwargs[key]
    return x

print(fun(a=2, b=3, c=5))









def fun(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

fun(1, 2, 3, x=4, y=5)