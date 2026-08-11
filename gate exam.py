x = 100
count = 0

while x > 1:
    x = x // 3
    count += 1

print(count)









A = [2, 4, 6, 8, 10, 12, 14]

print(A[1:6:2])






s = 0

for i in range(1, 4):
    for j in range(i, 4):
        s += 1

print(s)









def f(n):
    if n == 0:
        return 0
    return n + f(n-1)

print(f(4))









A = [1, 2, 3, 4, 5]

for i in range(len(A)):
    if A[i] % 2 == 1:
        A[i] = A[i] * 2

print(A)










x = 0
for i in range(1, 6):
    if i % 2 == 0:
        x += i
    else:
        x -= i

print(x)











A = [10, 20, 30, 40, 50]

A[1:4] = [5, 6]

print(A)












count = 0

for i in range(1, 5):
    for j in range(i):
        count += 1

print(count)






def fun(n):
    if n <= 1:
        return 1
    return n * fun(n - 2)

print(fun(5))