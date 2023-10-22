dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2]}

print("The original dictionary is : ", dict1)
res = list(sorted({ele for val in dict1.values() for ele in val}))

print("The unique values list is : ", res)