lista=[]
while True:
    tuote = input("Anna tuote: ")
    lista.append(tuote)


    if lista.count(tuote) == 2:
        del lista[-1]
        print("Kauppalista:"),
        print(*lista, sep = " ja ")
        break