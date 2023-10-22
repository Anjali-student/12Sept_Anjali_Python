number = int(input("Enter any number:"))
i = 1
num1 = 0
num2 = 1
next_num = num2

while i < number:
    num1, num2 = num2, next_num
    next_num = num1 + num2
    print(next_num, end=" ")
    i = i + 1

print(next_num)
