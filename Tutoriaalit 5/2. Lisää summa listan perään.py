lista = [1, 2, 1, 3]

summa = 0
for alkio in lista:
    summa += alkio

lista.append(summa)

print(lista)