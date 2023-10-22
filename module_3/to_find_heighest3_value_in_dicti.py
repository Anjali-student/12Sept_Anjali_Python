dict={'1':22,'2':44,'3':66,'4':88,'5':99}

lst=list()
for i in dict.values():
    lst.append(i)

lst.sort()
print("The Three Heighest values are:",lst[-1],lst[-2],lst[-3])

