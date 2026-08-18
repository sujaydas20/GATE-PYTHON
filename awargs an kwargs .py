def fun(*args):
    return sum(args)

print(fun(2, 4, 6))









def fun(a, *args):
    print(a)
    print(args[1])

fun(10, 20, 30, 40)