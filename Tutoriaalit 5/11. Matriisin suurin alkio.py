def suurin_alkio(matriisi: list) -> int:
    lista = []
    for rivi in matriisi:
        for alkio in rivi:
            lista.append(alkio)
    return max(lista)

print(suurin_alkio([[1, 2, 3],[6, 5, 4],[9, 7, 8]]))