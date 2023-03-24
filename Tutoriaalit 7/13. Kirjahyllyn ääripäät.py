kirjat = [('Mikki ja laakapallo', 1967, 289), ('Ressu ja Leevi', 1944, 228), ('Rokka ja Tikkanen', 1937, 198), ('Aku ja Robin', 1975, 322), ('Hulk ja superpähkinät', 1972, 310), ('Aku ja laakapallo', 1949, 254), ('Hulk ja Minni', 1966, 284), ('Ressu ja Robin', 1943, 218), ('Susikoira-Roi ja superpähkinät', 1926, 170), ('Vanhus ja kryptoniitti', 1959, 268), ('Nuorukainen ja Leevi', 1930, 177), ('Ressu ja Tikkanen', 1958, 261)]


def vanhin_kirja(kirjat: list) -> tuple:
    uusi = kirjat.copy()
    uusi.sort(key=lambda alkio: alkio[1])
    return uusi[0]

def uusin_kirja(kirjat: list) -> tuple:
    uusi = kirjat.copy()
    uusi.sort(key=lambda alkio: alkio[1])
    return uusi[-1]

def eniten_sivuja(kirjat: list) -> tuple:
    uusi = kirjat.copy()
    uusi.sort(key=lambda alkio: alkio[2])
    return uusi[-1]

def vahiten_sivuja(kirjat: list) -> tuple:
    uusi = kirjat.copy()
    uusi.sort(key=lambda alkio: alkio[2])
    return uusi[0]

print(eniten_sivuja(kirjat))
print(vahiten_sivuja(kirjat))