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








def fun(n):
    if n == 0:
        return 1
    return n * fun(n - 1)

print(fun(4))







s = 0

for i in range(1, 8):
    if i % 2 == 0:
        continue
    s += i

print(s)