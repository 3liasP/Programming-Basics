lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    luku = int(input("Anna luku: "))
    if luku == -1:
        print(f"Lista: {lista}")
        break
    indeksi = lista.index(luku)
    del lista[indeksi]
    print(f"Poistettiin luku {luku} indeksistä {indeksi}")