import os
from euklides import NWD
#from Sortowanie import *
import Sortowanie
#Clearing the Screenos.
os.system('cls')
liczba = int(input("Podaj pierwsza liczbe do sumy "))
liczba2 = int(input("Podaj druga liczbe do sumy "))
opcje = int(input("Wybierz Opcje 1- NWD, 2-Suma, 3-sortowanie "))
while opcje>=1 and opcje<=3:
    if opcje == 1:
        print("NWD:",NWD(liczba,liczba2))
    if opcje == 2:
        print("Suma:",liczba + liczba2)
    if opcje == 3:
        print("Sortowanie:",Sortowanie.babelkowe(tab = Sortowanie.losowanie_tablicy(5,0,99)))
    klawisz = input("Nacisnij dowolny klawisz aby kontynuowac\n")
    os.system('cls')
    opcje = int(input("Wybierz Opcje 1- NWD, 2-Suma, 3-sortowanie "))