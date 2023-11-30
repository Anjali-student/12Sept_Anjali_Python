with open('read1.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        secondfile.write(line )