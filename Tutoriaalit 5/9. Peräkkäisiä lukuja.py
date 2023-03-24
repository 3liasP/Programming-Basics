def perakkaisia(lista: list) -> int:
    pituus = len(lista)
    luku = 1
    perakkaisia = 0

    if luku in lista:
        luku += 1
        pituus -= 1
        perakkaisia = 1
    else:
        return perakkaisia
    perakkaisia += 1
    while pituus > 0:
        if luku in lista and (luku + 1) in lista:
            perakkaisia += 1
        else:
            break
        luku += 1
        pituus -= 1
    return perakkaisia

print(perakkaisia([12, 3, 4, 5, 1, 8, 9, 14, 10, 11, 2, 13]))