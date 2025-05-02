#### - uzupełnij tak oznaczone miejsca
'''
Swoje wyniki możesz sprawdzić porównując rezultat wydrukowany przez funkcję test.
Oczekiwany rezultat wykonania funkcji test:

ca.nastepny_wyraz(an=6) 8
ca.wyraz_z_wzoru_rekurencyjnego(n=4) 8
ca.tablica_wyrazow(n=8) [0, 2, 4, 6, 8, 10, 12, 14, 16]
['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
[' 0', ' 2', ' 4', ' 6', ' 8', '10', '12', '14', '16']
ca.tablica_wyrazow_wydruk(n=8)
 None
ca.wyraz_z_wzoru_ogolnego(n=4) 8
ca.ile_wyrazow(n1=3, n2=7) 5
ca.suma(n1=0, n2=8) 72.0
ca.wykres(n1=0, n2=8) None
ca.wykres_sumy(n1=0, n2=8) None
ca.wyraz_funkcja_rekurencyjna(n=4) 8
Zadania tekstowe
Na placu zebrało się 2138 osób. Pierwsza osoba wypowiedziała liczbę 7. Następnie każda kolejna osoba wypowiadała liczbę o 23 większą od poprzedniej. Jaką liczbę wypowie ostatnia osoba?
Odpowiedź: 49158
'''


import matplotlib.pyplot as plt


class arytmetyczny: # klasa ciągu arytmetycznego
    def __init__(self, a0, r):
        '''
        Ta funkcja nazywa się konstruktorem klasy. Wykona się w momencie utworzenia obiektu klasy arytmetyczny.
        Przykład utworzenia obiektu klasy arytmetyczny: ca = arytmetyczny(a0=0, r=2) <- parametry w nawiasach zostaną wykorzystane w funkcji konstruktora,
        tzn. wywoła się funkcja __init__(a0=0, r=2).
        Konstruktora używa się do przypisania parametrów ciągu arytmetycznego do pola obiektu (self.xxxx).
        def __init__(self, a0, r) <- parametry w nawiasach są widoczne tylko z poziomu tej funkcji
        self.xxxx <- pole obiektu, które jest widoczne z poziomu całej klasy, dzięki temu będziemy mogli odwołać się do niego z innych funkcji w tej samej klasie
        parametry:
        a0 - pierwszy wyraz ciągu
        r - różnica ciągu
        Definicja ciągu arytmetycznego: https://www.matemaks.pl/ciag-arytmetyczny.html
        '''
        self.a0 = ####
        ##########


    def nastepny_wyraz(self, an):
        '''
        Funkcja zwraca kolejny wyraz ciągu arytmetycznego.
        parametry:
        an - aktualny wyraz ciągu arytmetycznego, czyli wyraz o indeksie n
        return:
        kolejny wyraz ciągu arytmetycznego, czyli wyraz o indeksie n+1
        W tej funkcji należy uzupełnić wzór rekurencyjny ciągu arytmetycznego, czyli przepis na wyraz o indeksie n+1 w zależności od wyrazu o indeksie n.
        '''
        return ########
    

    '''
    W tym miejscu wypisz i rozpisz 8 pierwszych wyrazów ciągu arytmetycznego (a0=0, r=3) z wykorzystaniem wzoru rekurencyjnego
    a0 = 0
    a1 = a0 + 3 = 0 + 3 = 3
    a2 = a1 + 3 = 3 + 3 = 6
    a3 = ...
    a4 = ...
    a5 = ...
    a6 = ...
    a7 = ...
    a8 = ...
    '''
    

    '''
    W tym miejscu wypisz i rozpisz 8 pierwszych wyrazów ciągu arytmetycznego (a0=a0, r=r) z wykorzystaniem wzoru rekurencyjnego
    a0 = a0
    a1 = a0 + r
    a2 = a1 + r
    a3 = ...
    a4 = ...
    a5 = ...
    a6 = ...
    a7 = ...
    a8 = ...
    '''
    

    def wyraz_z_wzoru_rekurencyjnego(self, n):
        '''
        Funkcja zwraca wyraz ciągu arytmetycznego o indeksie n.
        Należy wykorzystać wzór rekurencyjny oraz ostatni znany nam wyraz ciągu arytmetycznego.
        '''
        ####### = self.a0
        for _ in range(######, ####):
            an = self.########(########)
        return ######
    

    def tablica_wyrazow(self, n):
        '''
        Wypełnia tablicę n wyrazami ciągu arytmetycznego.
        Indeks tablicy odpowiada indeksowi wyrazu ciągu arytmetycznego.
        '''
        a = [None for _ in range(######)]
        a[#####] = self.#####
        for i in range(######, #####):
            a[i] = self.#######(a[######])
        return a
    

    def tablica_wyrazow_wydruk(self, n):
        '''
        Drukuje dwie tablice: indeksów tych wyrazów wyrazów ciągu arytmetycznego.
        '''
        a = self.#######(#######)
        max_len = max( len(str(min(#######))), #####(###(#####(#######))) )
        a_text = [str(#####).rjust(max_len) for an in a]
        labels_text = [(##########).rjust(max_len) for i in range(n+1)]
        print(labels_text)
        print(a_text)


    '''
    W tym miejscu wypisz i rozpisz 8 pierwszych wyrazów ciągu arytmetycznego (a0=0, r=3) według schematu:
    a0 = 0
    a1 = 0 + 3 = 3
    a2 = a1 + 3 = (0 + 3) + 3 = 0 + 3 + 3 = 0 + 2*3
    a3 = ...
    a4 = ...
    a5 = ...
    a6 = ...
    a7 = ...
    a8 = ...
    '''
    

    '''
    W tym miejscu wypisz i rozpisz 8 pierwszych wyrazów ciągu arytmetycznego (a0=a0, r=r) według schematu:
    a0 = a0
    a1 = a0 + r
    a2 = a1 + r = (a0 + r) + r = a0 + r + r = a0 + 2r
    a3 = ...
    a4 = ...
    a5 = ...
    a6 = ...
    a7 = ...
    a8 = ...
    '''


    def wyraz_z_wzoru_ogolnego(self, n):
        '''
        Należy uzupełnić wzór ogólny na wyraz ciągu arytmetycznego,
        tzn. taki, który nie używa poprzednich wyrazów ciągu do obliczenia wyrazu o indeksie n.
        Zamiast tego można wykorzystać parametry ciągu arytmatycznego zapisane w polach self.xxxx
        '''
        return self.a0 + ############
    

    def ile_wyrazow(self, n1, n2):
        '''
        Funkcja zwraca ilość wyrazów ciągu arytmetycznego od n1 do n2 włącznie.
        n1, n2 - indeksy wyrazów ciągu arytmetycznego
        '''
        return abs(######-######) + #####


    def suma(self, n1, n2):
        '''
        Funkcja zwraca sumę wyrazów ciągu arytmetycznego od n1 do n2 włącznie.
        n1, n2 - indeksy wyrazów ciągu arytmetycznego
        '''
        an1 = self.wyraz_z_wzoru_ogolnego(####)
        an2 = self.##########(####)
        srednia12 = ########
        l = self.#######(#####, #####)
        return ####### * #####
    

    def wykres(self, n1, n2):
        '''
        Rysuje wykres wyrazów ciągu arytmetycznego od n1 do n2 włącznie.
        n1, n2 - indeksy wyrazów ciągu arytmetycznego
        '''
        a = self.#########(######)
        plt.plot(range(n1, n2+1), a[n1:n2+1])
        plt.title(r"$a_n = a_{n-1} + r$")
        plt.xlabel("n")
        plt.ylabel(r"$a_n$")
        plt.show()


    def wykres_sumy(self, n1, n2):
        '''
        Rysuje wykres sumy wyrazów ciągu arytmetycznego od n1 do n2 włącznie.
        n1, n2 - indeksy wyrazów ciągu arytmetycznego
        '''
        s = [None for _ in range(n2+1)]
        for i in range(n1, n2+1):
            s[i] = self.suma(#####, #####)
        plt.plot(range(n1, n2+1), s[n1:n2+1])
        plt.xlabel("n")
        plt.ylabel(r"$\sum_{n=n1}^{n2}a_n$".replace("n1", str(n1)).replace("n2", str(n2)))
        plt.show()


    def wyraz_funkcja_rekurencyjna(self, n):
        '''
        Funkcja zwraca wyraz ciągu arytmetycznego o indeksie n.
        Jest to funkcja rekurencyjna, to znaczy, że w jej ciele należy odwołać się do niej samej,
        tzn. w jej środku należy wywołać funkcję wyraz_funkcja_rekurencyjna(self, n)
        '''
        if n == 0:
            return #########
        return self.########(self.########(########))


    @staticmethod
    def zadania_tekstowe():
        print("Zadania tekstowe")
        print("Na placu zebrało się 2138 osób. Pierwsza osoba wypowiedziała liczbę 7. Następnie każda kolejna osoba wypowiadała liczbę o 23 większą od poprzedniej. Jaką liczbę wypowie ostatnia osoba?")
        odp1 = ##########################################
        print("Odpowiedź:", odp1)
    

    @staticmethod
    def test():
        ca = arytmetyczny(a0=0, r=2)
        print("ca.nastepny_wyraz(an=6)", ca.nastepny_wyraz(an=6))
        print("ca.wyraz_z_wzoru_rekurencyjnego(n=4)", ca.wyraz_z_wzoru_rekurencyjnego(n=4))
        print("ca.tablica_wyrazow(n=8)", ca.tablica_wyrazow(n=8))
        print("ca.tablica_wyrazow_wydruk(n=8)", "\n", ca.tablica_wyrazow_wydruk(n=8))
        print("ca.wyraz_z_wzoru_ogolnego(n=4)", ca.wyraz_z_wzoru_ogolnego(n=4))
        print("ca.ile_wyrazow(n1=3, n2=7)", ca.ile_wyrazow(n1=3, n2=7))
        print("ca.suma(n1=0, n2=8)", ca.suma(n1=0, n2=8))
        print("ca.wykres(n1=0, n2=8)", ca.wykres(n1=0, n2=8))
        print("ca.wykres_sumy(n1=0, n2=8)", ca.wykres_sumy(n1=0, n2=8))
        print("ca.wyraz_funkcja_rekurencyjna(n=4)", ca.wyraz_funkcja_rekurencyjna(n=4))
        ca.zadania_tekstowe()
    

class geometryczny:
    pass


class silnia:
    pass


class fibonacci:
    pass


def main():
    arytmetyczny.test()


if __name__ == "__main__":
    main()