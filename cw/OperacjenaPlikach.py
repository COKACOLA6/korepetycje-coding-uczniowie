f = open("PlikTekstowy.txt", "w")
f.write("ZawartośćPlików")
f.close()

with open("PlikTekstowy.txt", "r") as f:
    temp = f.read()
print(temp)

with open("PlikTekstowy.txt", "a") as f:
    f.write("cos")
