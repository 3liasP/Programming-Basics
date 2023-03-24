import random

def satunnaislista(pituus: int, alaraja: int, ylaraja: int) -> list:
    x = 0
    lista = []
    while x < pituus:
        lista.append(random.randint(alaraja, ylaraja))
        x += 1
    return lista

satunnaislista(5,1,10)