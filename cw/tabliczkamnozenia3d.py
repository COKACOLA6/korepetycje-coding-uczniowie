import random
import seaborn as sns
from matplotlib import pyplot as plt
random.seed(1) 
Cala = []
tab2D = []
tab1D = []
for k in range(3):
    for i in range(4):
        for j in range(5):
            x = random.random()
            #print(x)
            tab1D.append(x)
        tab2D.append(tab1D)
        tab1D = []
    Cala.append(tab2D)
    tab2D = []
print(Cala)


def Sortowanie(elements):
    size = len(elements)

    print("Before sorting:", elements)

    for i in range(size):
        for j in range(0, size-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                print(elements)

    print("After sorting:", elements)


a = Cala[0][0]
Sortowanie(a)


w1 = [0,1,2]
w2 = [0,1,2,3]
w3 = [0,1,2,3,4]


Cala = []
tab2D = []
tab1D = []
for k in range(3):
    for i in range(4):
        for j in range(5):
            x = w1[k] * w2[i] * w3[j]
            #print(x)
            tab1D.append(x)
        tab2D.append(tab1D)
        tab1D = []
    Cala.append(tab2D)
    tab2D = []
print(Cala)

plt.figure(figsize=(12,8))
sns.set(rc={'figure.figsize':(10,8)})
ax = sns.heatmap(Cala[0])