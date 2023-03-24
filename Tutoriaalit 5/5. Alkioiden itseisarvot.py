lista = [1, -1, 3, -2, -4, 1]

lista2 = [i*-1 if i < 0 else i for i in lista]

lista = lista2

print(lista)