def silnia(liczba):
    wynik = 1
    for i in range(1,liczba + 1):
        wynik *= i 
        print(wynik)
    return wynik
print(silnia(10))

"""
wynik5 = 5*4*3*2*1 = wynik4 * 5
wynik4 = 4*3*2*1 = wynik3 * 4
wynik3 = 3*2*1 = wynik2 * 3
wynik2 = 2*1 = wynik1 * 2
wynik1 = 1 = wynik0 * 1
wynik0 = 1
"""