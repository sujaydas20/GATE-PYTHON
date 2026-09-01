a = [1, 2, 3]
b = a

b.append(4)
a[0] = 10

print(a)
print(b)






def fun(a, b=2):
    return a * b

x = fun(5)
y = fun(5, 3)

print(x + y)