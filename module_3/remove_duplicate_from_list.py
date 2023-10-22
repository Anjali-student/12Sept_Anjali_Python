def remove():
    list1 = [2, 4, 10, 20, 5, 2, 20, 40]
    duplicate = []
    for i in list1:
        if i not in duplicate:
            duplicate.append(i)
    return duplicate


print(remove())
