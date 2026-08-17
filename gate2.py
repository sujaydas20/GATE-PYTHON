a = [10, 20, 30, 40, 50]
print(a[1:4])
print(a[::-1])









s = 0

for i in range(1, 10, 2):
    s += i

print(s)










a = [1, 2, 3]

b = a
b.append(4)

print(a)
print(b)








def add(x, y=5):
    return x + y

print(add(10))
print(add(10, 20))








def fun(n):
    if n == 0:
        return 0
    return n + fun(n - 1)

print(fun(4))








d = {
    "a": 10,
    "b": 20,
    "c": 30
}

d["b"] = d["b"] + 5

print(d["b"])








x = 1
s = 0

while x <= 5:
    if x % 2 == 0:
        s += x
    x += 1

print(s)








n = 4
count = 0

for i in range(n):
    for j in range(i + 1):
        count += 1

print(count)