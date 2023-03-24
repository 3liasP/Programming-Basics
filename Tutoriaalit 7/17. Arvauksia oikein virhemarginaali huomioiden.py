arvaukset = [8, 9, 22, 6, 5, 5, 13, 11, 11, 6, 7, 4, 1, 8, 2, 22]

def arvauksia_oikein(arvaukset: list, oikea: int, virhemarginaali=0):
    maara = 0
    for luku in arvaukset:
        if luku == oikea:
            maara += 1
        else:
            if luku in range (oikea - virhemarginaali, oikea + virhemarginaali + 1):
                maara += 1

    return maara

arvauksia_oikein(arvaukset, 8, 3)