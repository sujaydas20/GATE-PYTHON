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