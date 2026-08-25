def fun(x, y=2):
    return x * y

print(fun(5))
print(fun(5, 3))




a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)




a = [10, 20, 30, 40, 50]

print(a[1:4])
print(a[::-1])





def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))