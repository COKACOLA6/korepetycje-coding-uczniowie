import random
random.seed(1)
lista = []
for i in range(10):
    x = random.random()
    lista.append(x)

najwieksza_liczba = lista[0]
najmniejsza_liczba = lista[0]
for j in range(10):
    if najmniejsza_liczba > lista[j]:
        najmniejsza_liczba = lista[j]
    if najwieksza_liczba < lista[j]:
        najwieksza_liczba = lista[j]
print(lista)
print("Najmniejsza liczba w liscie to:",najmniejsza_liczba)
print("Najmniejsza wedlug pythona:",min(lista))
print("Najwieksza liczba to:",najwieksza_liczba)
print("Najwieksza liczba wedlug pythona:",max(lista))
idmax = lista.index(najwieksza_liczba)
idmin = lista.index(najmniejsza_liczba)
maxymalna = lista[idmax]
lista[idmax] = lista[idmin]
lista[idmin] = maxymalna
print(lista)