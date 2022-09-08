import random as r
import time
import matplotlib.pyplot as plt

def gen():
    num = r.randint(0,10)
    return num

numlist=[]
y_list = []

for i in range(0,10):
    test = gen()
    numlist.append(test)

for j in range(0,10):
    y_list.append(j)

plt.plot(y_list, numlist)
plt.show()