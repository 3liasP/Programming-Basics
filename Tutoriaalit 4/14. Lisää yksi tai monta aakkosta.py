def lisaa_seuraava(aakkosjono: str) -> str:
    aakkoset = ("abcdefghijklmnopqrstuvwxyzåäö")
    pituus = len(aakkosjono)
    aakkosjono = aakkosjono + aakkoset[pituus]
    return aakkosjono

def lisaa_monta(aakkosjono: str, maara: int) -> str:
    laskuri = 1
    while laskuri <= maara:
        uusi = lisaa_seuraava(aakkosjono)
        aakkosjono = uusi
        laskuri += 1
    
    return uusi
    
    


print(lisaa_seuraava("abc"))