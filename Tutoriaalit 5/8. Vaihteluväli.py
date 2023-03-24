lista = [-10, -7, -4, -1, 2, 5, 8]

def vaihteluvali(lista: list) -> int:
        vv = max(lista) - min(lista)
        return vv

print(vaihteluvali([-10, -7, -4, -1, 2, 5, 8]))