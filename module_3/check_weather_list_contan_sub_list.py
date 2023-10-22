test_list = [5, 6, 3, 8, 2, 1, 7, 1]

print("The original list : " + str(test_list))
sublist = [8, 2, 7, 8, 88, 2, 7]
c = 0
res = False
for i in sublist:
    if i in test_list:
        c += 1
if c == len(sublist):
    res = True
print("Is sublist present in list ? : " + str(res))
