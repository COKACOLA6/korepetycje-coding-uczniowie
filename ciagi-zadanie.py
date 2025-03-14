#### - uzupełnij tak oznaczone miejsca
import matplotlib.pyplot as plt


class arytmetyczny:
    def __init__(self, a0, r):
        self.a0 = a0
        self.r = r


    def nastepny_wyraz(self, an):
        return an+self.r
    

    def wyraz_z_wzoru_rekurencyjnego(self, n):
        an = self.a0
        for _ in range(1,n+1):
            an = self.nastepny_wyraz(an)
        return an
    

    def tablica_wyrazow(self, n):
        a = [None for _ in range(n+1)]
        a[0] = self.a0
        for i in range(1,n+1):
            a[i] = self.nastepny_wyraz(a[i-1])
        return a
    

    def tablica_wyrazow_wydruk(self, n):
        a = self.tablica_wyrazow(n)
        max_len = max( len(str(min(a))),len(str(max(a))))
        a_text = [str(an).rjust(max_len) for an in a]
        labels_text = [(i).rjust(max_len) for i in range(n+1)]
        print(labels_text)
        print(a_text)


    def wyraz_z_wzoru_ogolnego(self, n):
        return self.a0 + self.r * n
    

    def ile_wyrazow(self, n1, n2):
        return abs(######-######) + #####


    def suma(self, n1, n2):
        an1 = self.wyraz_z_wzoru_ogolnego(####)
        an2 = self.##########(####)
        srednia12 = ########
        l = self.#######(#####, #####)
        return ####### * #####
    

    def wykres(self, n1, n2):
        a = self.#########(######)
        plt.plot(range(n1, n2+1), a[n1:n2+1])
        plt.title(r"$a_n = a_{n-1} + r$")
        plt.xlabel("n")
        plt.ylabel(r"$a_n$")
        plt.show()


    def wykres_sumy(self, n1, n2):
        s = [None for _ in range(n2+1)]
        for i in range(n1, n2+1):
            s[i] = self.suma(#####, #####)
        plt.plot(range(n1, n2+1), s[n1:n2+1])
        plt.xlabel("n")
        plt.ylabel(r"$\sum_{n=n1}^{n2}a_n$".replace("n1", str(n1)).replace("n2", str(n2)))
        plt.show()


    def wyraz_funkcja_rekurencyjna(self, n):
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
'''
a0 = a0
a1 = a0 + r
a2 = a1 + r = a0 + r + r
a3 = a2 + r = a0 + r + r + r
a4 = a3 + r = a0 + r + r + r + r
a5 = a4 + r = a0 + r + r + r + r + r
an = a0 + rn = a0 + r * n






'''