def comman(list1, lit2):
    result = False
    for i in list1:
        for j in lit2:
            if i == j:
                result = True
    return result


print(comman([1, 2, 3, 4], [4, 5, 6]))
