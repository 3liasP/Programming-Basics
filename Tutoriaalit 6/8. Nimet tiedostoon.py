with open("nimet.txt", "w") as tiedosto:
    nimi = input("Anna nimi: ")
    tiedosto.write(nimi + "\n")
    while True:
        nimi = input("Anna nimi: ")
        if nimi == "":
            break
        tiedosto.write(nimi + "\n")
