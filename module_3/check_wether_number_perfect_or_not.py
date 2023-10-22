def number_check(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


print(number_check(10))