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
        if rivi[0] == "L":
            muuttujat[rivi[4]] = rivi[rivi.find("=")+1:]
        elif rivi[0] == "P":
            palautus = palautus + muuttujat[rivi[len(rivi)-1]] + "\n"
    return palautus

suorita()