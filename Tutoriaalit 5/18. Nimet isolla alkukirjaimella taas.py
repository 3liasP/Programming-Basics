nimilista = ["maarit", "janne", "pekka", "joose", "petteri", "juudas", "jeesus", "arkhimedes"]


def nimet_isolla(nimilista: list):
    global uusi_nimilista
    uusi_nimilista  = []
    for nimi in nimilista:
        nimilman = nimi.replace(nimi[0], "", 1)
        alku = nimi[0].upper()
        nimi = alku + nimilman
        uusi_nimilista.append(nimi)
    nimilista = uusi_nimilista

nimet_isolla(nimilista)
print(nimilista)