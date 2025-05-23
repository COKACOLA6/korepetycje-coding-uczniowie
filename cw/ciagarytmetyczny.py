def ciag(a0,r,n):
    a = [None for _ in range(n+1)]
    a[0] = a0
    for i in range(n):
        a[i+1] = a[i] + r
    etykietki = ["a" + str(i) for i in range(n+1)]
    print(etykietki)
    print(a)
    return a[-1]
wynik = ciag(1000,5,5)
print("Wynik:",wynik)
a0 = 1000
r = 5
n = 5
print([a0 + r * i for i in range(n+1)])
"""
a[n+1] = a[n] + r = a0 + r * (n + 1)
a[n] = a[n-1] + r = a0 + r * n 
a[5] = a0 + r + r + r + r + r = a0 + r * 5
a[4] = a0 + r + r + r + r = a0 + r * 4
a[3] = a0 + r + r + r = a0 + r * 3 
a[2] = a0 + r + r = a0 + r * 2
a[1] = a0 + r = a0 + r * 1
a[0] = a0 = a0 + r * 0
"""