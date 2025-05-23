text_poczatkowy = "5 9\n2 5\n91 63\n52 68\n10 198"

with open("Wejscie.txt", "w") as f:
    f.write(text_poczatkowy)

# Odczytaj linie, oblicz sumy i zapisz do nowego pliku
with open("Wejscie.txt", "r") as f:
    temp = f.read().split("\n")

with open("Wejscie.txt", "w") as f:
    for line in temp:
        if line.strip() == "":
            continue
        skladniki = line.split(" ")
        suma = int(skladniki[0]) + int(skladniki[1])
        nowa_linia = f"{line} {suma}\n"
        f.write(nowa_linia)

with open("Wejscie.txt", "r") as f:
    print("Ostateczny plik")
    print(f.read())