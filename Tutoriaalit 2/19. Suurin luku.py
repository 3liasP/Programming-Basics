
isoin = 0

while True:
    luku = int(input("Anna luku: "))
    if luku > isoin:
        isoin = luku

    if luku == 0:
        print("Suurin luku on", isoin)
        break