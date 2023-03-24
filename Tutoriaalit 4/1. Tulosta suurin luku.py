def suurin_luku(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("Suurin luku on", n1)
    if n2 > n1 and n2 > n3:
        print("Suurin luku on", n2)
    if n3 > n1 and n3 > n2:
        print("Suurin luku on", n3)

suurin_luku(95, 209, 181)