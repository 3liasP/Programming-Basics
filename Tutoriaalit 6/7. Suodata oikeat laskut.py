def oikeat_vastaukset() -> list:
    with open("laskut.csv") as tiedosto:
        oikeat_laskut = []
        for rivi in tiedosto: 
            korjattu_rivi = rivi.replace("=", "+")
            tiedot_rivilla = korjattu_rivi.strip().split("+")
            eka = int(tiedot_rivilla[0])
            toka = int(tiedot_rivilla[1])
            vastaus = int(tiedot_rivilla[2])
            lasku = eka + toka
            if lasku == vastaus:
                oikeat_laskut.append(f"{eka} + {toka} = {vastaus}")
    return oikeat_laskut

print(oikeat_vastaukset())