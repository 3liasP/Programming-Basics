luvut = [5, 4, 8, 7, 6, 1]

def kertomat(luvut: list) -> dict:
    sanakirja = {}
    fact = 1
    for luku in luvut:
        for i in range (luku, luku+1):
            fact = fact * i
            sanakirja[fact] = i
    return sanakirja

print((kertomat(luvut)))