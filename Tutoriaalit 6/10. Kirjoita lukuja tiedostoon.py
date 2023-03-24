lista = [1,2,3,4,5,6,7,8]

def kirjoita_luvut(luvut:list, lukuja_riville: int):
    x = 1
    rivi = ""
    with open("luvut.csv", "w") as tiedosto:
        rivi += str(luvut[0])
        while True:
            while x > lukuja_riville:
                rivi += f"{luvut[x]},"
                x += 1
            tiedosto.write(rivi)
            if x == len(lista):
                break
            


"""
        while x <= riveja:
            rivi = sarakkeita * f"{arvo},"
            rivi = rivi[:-1]
            rivi += "\n"
            tiedosto.write(rivi)
            x += 1
"""
kirjoita_luvut(lista, 3)