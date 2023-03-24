lista = []

while True:
    luku = int(input("Anna luku: "))
    if luku == -1:
        print(f"Lista: {lista}")
        break
    lista.append(luku)