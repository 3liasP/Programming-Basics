ika = int(input("Anna ikä: "))

if ika < 18:
    print("Odota vielä", 18 - ika, "vuotta")
else:
    kpl = int(input("Kuinka monta? "))
    if kpl >= 5:
        print("Hinta yhteensä:", kpl * 39.9)
    else:
        print("Hinta yhteensä:", kpl * 49.9)