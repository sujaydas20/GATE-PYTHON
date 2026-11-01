d = {"a": 1, "b": 2, "c": 3}

v = d.keys()
d["d"] = 4
d.pop("b")

print(list(v))




from operator import methodcaller

words = ["apple", "BANANA", "cherry"]
f = methodcaller("lower")

result = list(map(f, words))
print(result[1][2:])





a = [[1, 2, 3], [4, 5, 6]]
b = list(zip(*a))

print(b[1][0] + b[2][1])




from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b == Decimal("0.3"))



def f(s):
    if len(s) <= 1:
        return s
    return f(s[2:]) + s[1]

print(f("ABCDEFG"))




from collections import UserDict

class D(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

d = D()
d["x"] = 3
d["y"] = d["x"] + 1

print(d["x"] + d["y"])


from enum import IntEnum

class Level(IntEnum):
    LOW = 1
    MID = 2
    HIGH = 3

x = Level.MID

print(x + 2, x == 2, x is 2)


class A:
    def __init__(self, x):
        self.x = x
    def __delattr__(self, name):
        if name == 'x':
            object.__setattr__(self, 'x', 99)

a = A(10)
del a.x
print(a.x)






print(round(2.5), round(3.5), round(4.5))




a = [1, 2, 3, 4]
a[1:3] = [8, 9, 10]
print(a[2], len(a))




from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 3)
p2 = p1._replace(y=7)
print(p1.x + p2.y)




from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 3)
p2 = p1._replace(y=7)
print(p1.x + p2.y)





import re
s = 'gate2027'
result = re.sub(r'(\D+)(\d+)', r'\2-\1', s)
print(result)





import re
s = 'gate2027'
result = re.sub(r'(\D+)(\d+)', r'\2-\1', s)
print(result)