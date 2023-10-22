str1="the lyrics is not that poor"
snot = str1.find('not')
spoor = str1.find('poor')

if spoor > snot > 0 and spoor > 0:
    str1 = str1.replace(str1[snot:(spoor + 4)],'good')
    print(str1)
else:
    print(str1)
