list = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in list:
    d.setdefault(a, []).append(b)
print (d)