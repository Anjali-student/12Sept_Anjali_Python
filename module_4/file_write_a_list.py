import random

data=[]
fl=open('read2.txt','a')
n=int(input("Enter number of Students:"))

for i in range(n):

    name=input("Enter your name:")
    data.append(name)

print(data)
fl.write(f"Name:{data}\n")