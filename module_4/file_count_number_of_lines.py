with open('read1.txt', 'r') as file:
    i=0
    for line in file:
        line = line.strip()
        i=i+1
print("the number of line is: ",i)
