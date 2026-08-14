# # def count(child_dict, i):
# #     if i not in child_dict.keys():
# #         return 1

# #     ans = 1

# #     for j in child_dict[i]:
# #         ans += count(child_dict, j)

# #     return ans


# # child_dict = dict()

# # child_dict[0] = [1, 2]
# # child_dict[1] = [3, 4, 5]
# # child_dict[2] = [6, 7, 8]

# # print(count(child_dict, 0))















# def fun(D, S_1, S_2):
#     if S_1 < S_2:
#         D[S_1], D[S_2] = D[S_2], D[S_1]
#         fun(D, S_1 + 1, S_2 - 1)














# def func(A, n, m):
#     s = A[0]

#     for i in range(1, n-1):
#         m = m * s + A[i]

#     return m
        




count = 0

for i in range(1, 5):
    for j in range(i):
        count += 1

print(count)













d = {'a': 10, 'b': 20}

d['a'] = d['a'] + 5
d['c'] = d['b'] + 10

print(d)











x = 0

for i in range(2, 10, 2):
    x = x + i

print(x)






a = [10, 20, 30, 40, 50, 60]
print(a[1:5:2])







x = 0

for i in range(3):
    for j in range(i + 1):
        x += 1

print(x)








def change(a):
    a.append(10)

x = [1, 2, 3]
change(x)

print(x)







def fun(n):
    if n == 0:
        return 0
    return n + fun(n - 1)

print(fun(4))






s = "GATE"
print(s[-1] + s[1])








d = {"a": 10, "b": 20, "c": 30}

d["b"] = d["a"] + d["c"]

print(d["b"])








a = [1, 2, 3, 4, 5]

b = [x * x for x in a if x % 2 == 0]

print(b)