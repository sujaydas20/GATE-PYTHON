def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

print(f(6))




def f(a):
    a[1] = a[0] + a[2]
    return a

x = [2, 4, 6]
y = f(x)

print(x)
print(y)





def f(a, b=10):
    return a + b

x = f(5)
y = f(5, 20)

print(x + y)



count = 0

for i in range(4):
    for j in range(i):
        count += 1

print(count)



# def f(n):
#     if n == 0:
#         return 0
#     return n + f(n-2)

# print(f(9))



def f(d):
    d["x"] = d["a"] + d["b"]
    return d

d = {"a": 2, "b": 3}
x = f(d)

print(d["x"])






a = [1, 2, 3, 4, 5, 6]

x = a[::2]
y = a[::-2]

print(x)
print(y)






def f(n):
    if n <= 0:
        return 0
    return n + f(n - 2)

print(f(9))





def f(n):
    if n <= 1:
        return 1
    return n + f(n - 2)

print(f(6))




def f(a):
    a.append(5)
    return a

x = [1, 2]
y = f(x)

print(x)
print(y)




def f(x):
    if x % 2 == 0:
        return x * 2
    return x + 2

print(f(4))
print(f(5))





x = 10

def f():
    x = 20

    def g():
        return x + 5

    return g()

print(f())



def f(n):
    if n <= 0:
        return 0
    return n + f(n - 2)

print(f(7))




a = [10, 20, 30, 40, 50]

print(a[1:4])
print(a[4:1:-1])




def f(n):
    s = 0
    for i in range(1, n):
        if i % 2 == 0:
            s += i
    return s

print(f(8))