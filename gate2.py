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