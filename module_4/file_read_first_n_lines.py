file = open('read1.txt', 'r')

for line in file:
    first_line = line
    break

print("First line:", first_line)
file.close()