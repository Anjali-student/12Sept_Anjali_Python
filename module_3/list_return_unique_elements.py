def unique1(list1):
    x = []
    for i in list1:
        if i not in x:
            x.append(i)
    return x


print(unique1([1, 2, 3, 3, 3, 3, 4, 5]))
