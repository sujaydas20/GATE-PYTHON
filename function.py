def fun(a, b=5):
    return a + b

print(fun(10))





def fun(a, b):
    a = a + 2
    b = b + 3
    return a * b

print(fun(3, 4))





x = 10

def fun():
    x = 20
    return x

print(x)







def f(x):
    return x + 2

def g(x):
    return f(x) * 2

print(g(3))





def fun(a):
    a.append(4)

x = [1, 2, 3]
fun(x)

print(x)









def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4))







def fun(**kwargs):
    return kwargs["a"] + kwargs["b"]

print(fun(a=10, b=20))









def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))









def fun(a, b=5):
    return a + b

print(fun(10))
print(fun(10, 20))








def fun(a, b):
    return a+b, a*b

x, y = fun(3, 4)

print(x)
print(y)






x = 10

def fun():
    x = 20
    print(x)

fun()
print(x)




def fun(a):
    a.append(5)

x = [1, 2, 3]
fun(x)

print(x)







def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))





def f(x):
    return x + 2

def g(x):
    return f(x) * 2

print(g(3))





def fun(*args):
    return sum(args)

print(fun(1, 2, 3))
print(fun(4, 5))