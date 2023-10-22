x = ("apple", "banana", "cherry")
y = list(x)
y[-1] = "Guava"
x = tuple(y)
print(x)