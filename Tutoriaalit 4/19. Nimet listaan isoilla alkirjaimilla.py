lista = []

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        print(f"Nimet: {lista}")
        break
    nimilman = nimi.replace(nimi[0], "", 1)
    alku = nimi[0].upper()
    nimi = alku + nimilman
    lista.append(nimi)