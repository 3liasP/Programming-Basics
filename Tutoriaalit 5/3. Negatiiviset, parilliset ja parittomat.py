lista = []
negatiiviset = []
parilliset = []
parittomat = []
while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        break
    else:
        lista.append(luku)

for alkio in lista:
    if alkio < 0:
        negatiiviset.append(alkio)
    elif alkio % 2 == 0:
        parilliset.append(alkio)
    else:
        parittomat.append(alkio)

print("Negatiiviset:")
for alkio in negatiiviset:
    print(alkio)

print("Parilliset:")
for alkio in parilliset:
    print(alkio)

print("Parittomat:")
for alkio in parittomat:
    print(alkio)