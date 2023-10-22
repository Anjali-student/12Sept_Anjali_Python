str1 = input("Enter the sentence:")
counts = dict()
words = str1.split()
for i in words:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)
