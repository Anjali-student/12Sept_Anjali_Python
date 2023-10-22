string = input("Enter your string:")
if len(string) <= 2:
    print("NULL")
else:
    string1 = (string[:2] + string[-2:])
    print("The Original String is:",string)
    print("After concatenation string:",string1)
