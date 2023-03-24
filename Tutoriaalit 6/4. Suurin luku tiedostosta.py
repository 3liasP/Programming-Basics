def suurin_luku() -> int:
    with open("luvut.txt") as tiedosto:
        luvut = []
        for rivi in tiedosto:
            luvut_rivilla = rivi.strip().split(",")
            for pala in luvut_rivilla:
                luvut.append(int(pala))
    return max(luvut)