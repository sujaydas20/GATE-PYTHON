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




x = 5
y = 10

print(x < y and y > 7)
print(x > y or x == 5)





d = {1: "A", 2: "B", 3: "C"}

d[2] = "X"

print(d[2])
print(len(d))









s = 0

for i in range(1, 6, 2):
    s += i

print(s)