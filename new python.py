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