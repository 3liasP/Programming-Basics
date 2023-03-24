pisteet1 = 0
pisteet2 = 0


while True:

    #muuttujat
    pelaaja1 = ""
    pelaaja2 = ""

    #kysymykset
    pelaaja1 = input("Pelaaja 1 valinta: ")
    if pelaaja1 == "":
            break
    pelaaja2 = input("Pelaaja 2 valinta: ")

    #pelin interaktiot
    if pelaaja1 == "sakset" and pelaaja2 == "paperi":
        print("Pelaaja 1 voitti")
        pisteet1 += 1

    if pelaaja1 == "sakset" and pelaaja2 == "kivi":
        print("Pelaaja 2 voitti")
        pisteet2 += 1

    if pelaaja1 == "sakset" and pelaaja2 == "sakset":
        print("Tasapeli")

    if pelaaja1 == "kivi" and pelaaja2 == "sakset":
        print("Pelaaja 1 voitti")
        pisteet1 += 1

    if pelaaja1 == "kivi" and pelaaja2 == "paperi":
        print("Pelaaja 2 voitti")
        pisteet2 += 1

    if pelaaja1 == "kivi" and pelaaja2 == "kivi":
        print("Tasapeli")

    if pelaaja1 == "paperi" and pelaaja2 == "kivi":
        print("Pelaaja 1 voitti")
        pisteet1 += 1

    if pelaaja1 == "paperi" and pelaaja2 == "sakset":
        print("Pelaaja 2 voitti")
        pisteet2 += 1

    if pelaaja1 == "paperi" and pelaaja2 == "paperi":
        print("Tasapeli")

#Pelin jälkeen:

print("Peli loppui")
print("Pelaaja 1 sai", pisteet1, "pistettä")
print("Pelaaja 2 sai", pisteet2, "pistettä")