nopeus = int(input("Anna nopeus km/h: "))
matka = int(input("Anna matka: "))
turbo = input("Onko turboboost k/e: ")

if turbo == "k":
    print("Matka taittuu", (matka / (2*nopeus)), "tunnissa." )

if turbo == "e":
    print("Matka taittuu", (matka / nopeus), "tunnissa.")90