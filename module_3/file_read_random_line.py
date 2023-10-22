import random

x=open('test.txt','r').read().splitlines()

print(random.choice(x))
