def NWD (a,b):
    while a!=b:
        if a>b:
            a= a-b
        else:
            b = b-a
    return a
    

a = int(input("podaj a:"))
b = int(input("Podaj b:"))
print("NWD",NWD(a,b))