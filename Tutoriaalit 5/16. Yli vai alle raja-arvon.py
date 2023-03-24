tulokset = [("Jarmo", 5, 6, 5), ("Jaana", 8, 9, 9), ("Liisa", 6, 8, 7)]

def yli_vai_alle(tulokset: list, raja: int) -> tuple:
    lista = []
    for rivi in tulokset:
        rivi_lista = list(rivi)
        lista.append(rivi_lista)
    # lista on nyt matriisi
    pelkat_numerot = []
    for i in lista:
        for alkio in i:
            

yli_vai_alle(tulokset, 7)