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