a = 10
b = 20
print(f"Before swapping the value of a=", a, "and b=", b)
temp = a
a = b
b = temp
print(f"After swapping the value of a=", a, "and b=", b)
print("Swapping without using temp variable")
(a, b) = (b, a)
print(f"After swapping the value of a=", a, "and b=", b)
