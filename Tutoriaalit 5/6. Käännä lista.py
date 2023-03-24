lista = [1, -1, 3, -2, -4, 1]
pituus = len(lista)
ekaindeksi = 1
vikaindeksi = -1
lista2 = []
while pituus > 0:
    vika = lista[vikaindeksi]
    lista2.append(vika)
    lista.pop
    vikaindeksi -= 1
    pituus -= 1

lista = lista2
print(lista)