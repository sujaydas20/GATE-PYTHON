numbers = [1, 2, 3, 2, 4, 1, 2, 5, 3, 1]

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)



x = 1
s = 0

while x <= 10:
    s += x
    if s > 10:
        break
    x += 2

print(s)





d = {i: i*i for i in range(1, 5)}

print(d[2] + d[4])





s = "GATE2027"

print(s.count("2") + len(s))





a = [1, 2, 3, 4]

b = list(map(lambda x: x * 2 + 1, a))

print(b[1] + b[3])




a = [2, 5, 8, 11, 14]

b = list(filter(lambda x: x % 3 == 2, a))

print(sum(b))








a = 2 + 3 * 4 ** 2 // 5

print(a)




a = [[1, 2], [3, 4]]
b = a.copy()

b[0][1] = 10

print(a)
print(b)




d = {i: i*i for i in range(1, 5)}

print(d[2] + d[4])





{i: i*i for i in range(1, 5)}





a = [[1, 2], [3, 4]]
b = a.copy()

b[0][1] = 10

print(a)
print(b)




a = 17
b = 5

print(a // b)
print(a % b)




a = [1, [2, 3], 4]

a[1].append(5)

print(a)



a = [10, 20, 30]

s = 0

for i, x in enumerate(a):
    s += i * x

print(s)




a = {1, 2, 3, 4}
b = {2, 4, 6}

print(len(a & b))





s = "GATE"

t = s
t = t + "2027"

print(s)
print(t)


a = [2, 4, 6, 7]

print(any(x % 2 == 1 for x in a))
print(all(x % 2 == 0 for x in a))





def f(*args):
    s = 0
    for x in args:
        if x > 3:
            s += x
    return s

print(f(1, 4, 2, 6, 3, 5))






a = [1, 2, 3]
b = [4, 5, 6]

s = 0

for x, y in zip(a, b):
    s += x * y

print(s)








a = [2, 4, 6, 8]

x = 5 in a
y = 6 in a

print(x or y)






for i in range(3):
    print(i, end=" ")

else:
    print("Done")






a = [7, 2, 9, 4, 6]

x = max(a) - min(a)

print(x)    





a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(a[1][0] + a[2][1])




f = lambda x, y: x if x > y else y

print(f(7, 4) + f(2, 9))





try:
    x = 10 // 0
except ZeroDivisionError:
    x = 5

print(x)