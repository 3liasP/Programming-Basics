matriisi = [[1, 2], [3, 4]]

lista = []
laskuri = 1

for rivi in matriisi:
    summa = sum(rivi)
    rivi.append(summa)
    lista.append(rivi)
matriisi = lista
print(matriisi)