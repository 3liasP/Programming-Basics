kirjat = {"mjh-500": ("Mikki ja Hessu", 1987, 104, True), "ajr-600": ("Aku ja Roope", 1999, 120, True), "vlj-700": ("Veljenpojat", 2009, 179, True)}

def kirjat_tiedostoon(kirjat: dict, tiedoston_nimi: str):
    with open(f"{tiedoston_nimi}", "w") as tiedosto:
        for kirja in kirjat:
            avain = str(kirja)
            tiedot = str(kirjat[kirja])
            rivi = f"{avain},{tiedot}"
            rivi = rivi.replace("(","")
            rivi = rivi.replace(")","")
            rivi = rivi.replace(", ",";")
            rivi = rivi.replace("'","")
            rivi = rivi.replace(",",";")
            tiedosto.write(f"{rivi}\n")

kirjat_tiedostoon(kirjat, "kirjat.txt")


'''
toka = kirjat[kirja]
            tokastr = ""
            for i in toka:
                tokastr += str(tokastr) + str(i)
            print(tokastr)
            ekastr = "".join(eka)
            tokastr = "".join(toka)
            rivi = ekastr + tokastr
            print(rivi)
'''