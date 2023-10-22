number = int(input('Enter number for Factorial:'))
factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i = i + 1
print('\f factorial of ' + str(number) + ' is ' + str(factorial))
