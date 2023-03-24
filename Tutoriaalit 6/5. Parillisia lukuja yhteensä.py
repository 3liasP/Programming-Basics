def parillisia_yhteensa() -> int:
    with open("luvut1.txt") as tiedosto:
        luvut1 = []
        for rivi in tiedosto:
            luvut_rivilla = rivi.strip().split(",")
            for pala in luvut_rivilla:
                luvut1.append(int(pala))
    with open("luvut2.txt") as tiedosto:
        luvut2 = []
        for rivi in tiedosto:
            luvut_rivilla = rivi.strip().split(",")
            for pala in luvut_rivilla:
                luvut2.append(int(pala))
    parilliset = 0
    for luku in luvut1:
        if luku % 2 == 0:
            parilliset += 1
    for luku in luvut2:
        if luku % 2 == 0:
            parilliset += 1
    return parilliset

print(parillisia_yhteensa())