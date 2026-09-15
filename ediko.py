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