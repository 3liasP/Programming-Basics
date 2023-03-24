from datetime import datetime

def paivat_ennen(paivat: list, raja: datetime) -> list:
    lista = []
    for paiva in paivat:
        if paiva < raja:
            lista.append(paiva)
    return lista
