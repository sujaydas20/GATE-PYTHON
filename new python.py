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