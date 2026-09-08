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