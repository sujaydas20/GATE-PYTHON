def f(n):
    if n <= 1:
        return n
    return f(n-1) + 2*f(n-2)

print(f(5))



def f(a):
    a[0] = a[1] + 5
    return a

x = [2, 4, 6]
y = f(x)

print(x)
print(y)




def f(n):
    s = 0
    for i in range(1, n, 2):
        s += i
    return s

print(f(10))




x = 5

def f():
    x = 10
    return x + 2

print(f())
print(x)





def f(n):
    if n <= 0:
        return 1
    return n * f(n-2)

print(f(6))




a = [1, 2, 3, 4, 5, 6, 7]

x = a[1:6:2]
y = a[::-3]

print(x)
print(y)



def f(d):
    d["c"] = d["a"] * d["b"]
    d["a"] = d["c"] - d["b"]
    return d

x = {"a": 2, "b": 4}
y = f(x)

print(y)





def f(n):
    if n <= 0:
        return 0
    return n + f(n-3)

print(f(10))




def f(a):
    for i in range(len(a)):
        a[i] = a[i] + i
    return a

x = [1, 2, 3, 4]
print(f(x))




def f(n):
    if n <= 1:
        return 1
    return n * f(n-2)

print(f(7))




x = 10

def f():
    x = 20
    def g():
        return x + 5
    return g()

print(f())
print(x)




a = [2, 4, 6, 8, 10, 12]

x = a[1:5:2]
y = a[-1:1:-2]

print(x)
print(y)



d = {"a": 2, "b": 3}

d["a"] = d["a"] + d["b"]
d["b"] = d["a"] * d["b"]

print(d)



def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-3)

print(f(5))




def f(n):
    if n <= 0:
        return 0
    return n + f(n-3)

print(f(10))



def f(n):
    if n <= 0:
        return 0
    return n + f(n-2)

print(f(8))



def f(a):
    a[0] = a[-1] + 2
    return a

x = [3, 5, 7]
y = f(x)

print(x)
print(y)



def f(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            s += i
    return s

print(f(7))



x = 5

def f():
    x = 10

    def g():
        return x + 2

    return g()

print(f())
print(x)





def f(n):
    if n <= 1:
        return 1
    return n * f(n-2)

print(f(8))



a = [10, 20, 30, 40, 50, 60]

x = a[::2]
y = a[5:0:-2]

print(x)
print(y)