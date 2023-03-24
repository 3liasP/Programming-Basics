suurin = int(0)
pienin = int(0)

while True:
    luku = int(input("Anna luku: "))

    if luku > suurin:
        suurin = luku

    if luku < pienin:
        pienin = luku

    if luku == 0:
        print("Suurin luku on", suurin)
        print("Pienin luku on", pienin)
        break