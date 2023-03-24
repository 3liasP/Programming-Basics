def suorita(koodi: str) -> str:
    rivit = koodi.strip().split("\n")
    palautus = ""
    muuttujat = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    }
    for rivi in rivit:
        if rivi.find("LET") == 0:
            muuttujat[rivi[4]] = rivi[rivi.find("=")+1:]
        elif rivi.find("PRINT") == 0:
            palautus = palautus + muuttujat[rivi[len(rivi)-1]] + "\n"
        elif rivi.find("INC") == 0:
            uusiRivi = rivi.strip().split(" ")
            if uusiRivi[2].isnumeric() == True:
                muuttujat[uusiRivi[1]] = str(int(muuttujat[uusiRivi[1]]) + int(uusiRivi[2]))
            elif uusiRivi[2].isalpha() == True:
                muuttujat[uusiRivi[1]] = str(int(muuttujat[uusiRivi[1]]) + int(muuttujat[uusiRivi[2]]))
        elif rivi.find("DEC") == 0:
            uusiRivi = rivi.strip().split(" ")
            if uusiRivi[2].isnumeric() == True:
                muuttujat[uusiRivi[1]] = str(int(muuttujat[uusiRivi[1]]) - int(uusiRivi[2]))
            elif uusiRivi[2].isalpha() == True:
                muuttujat[uusiRivi[1]] = str(int(muuttujat[uusiRivi[1]]) - int(muuttujat[uusiRivi[2]]))
    return palautus

print(suorita("LET d=1000\nLET a=100\nLET b=10\nLET c=1\nINC d a\nINC d b\nINC d c\nPRINT d\nDEC d a\nDEC d b\nDEC d c\nPRINT d"))