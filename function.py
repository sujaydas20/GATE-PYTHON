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