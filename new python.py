d = {"a": 1, "b": 2, "c": 3}

v = d.keys()
d["d"] = 4
d.pop("b")

print(list(v))