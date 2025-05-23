tab =  []
n = 0
for i in range(11):
    tab.append(n)
    n+=1
print(tab)
tab2 = []
m = 0
for i in range(21):
    tab2.append(m)
    m+=1
print(tab2)
duzatablica = []
for i in range(len(tab)):
    tab4 = []
    for j in range(len(tab2)):
        tab4.append(tab2[j] * tab[i])
    duzatablica.append(tab4)
def wypisywanie(duzatablica):
    naglowek = []
    for j in range(len(duzatablica[1])):
        naglowek.append(f"{duzatablica[1][j]:>5}")
    print(" " * 5,"|",naglowek)
    print("_" * 5 ,"|","_" * len(duzatablica[0])*9)
    for i in range(len(duzatablica)):
        tab4 = []
        for j in range(len(duzatablica[0])):
            tab4.append(f"{duzatablica[i][j]:>5}")
        print(tab4[1],"|",tab4)
wypisywanie(duzatablica)