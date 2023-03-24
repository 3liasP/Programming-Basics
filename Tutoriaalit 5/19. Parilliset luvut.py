lukulista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def parilliset(lukulista: list) -> list:
    uusilista = []
    for luku in lukulista:
        if luku % 2 == 0:
            uusilista.append(luku)
    return uusilista

print(parilliset(lukulista))