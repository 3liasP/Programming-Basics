def kirjoita_matriisi(riveja: int, sarakkeita: int, arvo: int):
    x = 1
    with open("matriisi.csv", "w") as tiedosto:
        while x <= riveja:
            rivi = sarakkeita * f"{arvo},"
            rivi = rivi[:-1]
            rivi += "\n"
            tiedosto.write(rivi)
            x += 1

kirjoita_matriisi(3, 4, 7)