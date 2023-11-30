file = open('read1.txt', 'r')

for line in file:
    first_line = line

print("First line:", first_line)
file.close()