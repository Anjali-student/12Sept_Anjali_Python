with open('read1.txt', 'r') as file:
    f1=file.read()
word= (f1.split())
long_word=max(word,key=len)
print("the longest word in 1st line=",long_word)
