with open('read1.txt', 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)
print(lines)
