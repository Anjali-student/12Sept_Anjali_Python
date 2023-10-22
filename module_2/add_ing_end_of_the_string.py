str = input("Enter the string:")

if len(str) < 3:
    print(f'As the string length is less than 3 so expected result {str}')
else:
    if str[-3:] == 'ing':
        new_str = str + 'ly'
        print(f'Expected result: {new_str}')
    else:
        new_str = str + 'ing'
        print(f'Expected result: {new_str}')


