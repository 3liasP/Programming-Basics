lista = []

while True:
    try:
        nimi = input("Nimi: ")
        if nimi == "":
            print(f"Lista: {lista}")
            break
        vuosi = int(input("Syntymävuosi: "))    
        if len(nimi) < 2:
            print("Nimi on liian lyhyt!")
            if vuosi < 1800:
                    print("Olet liian vanha!")
            if vuosi > 2021:
                print("Et ole vielä syntynyt!")
        elif vuosi < 1800:
            print("Olet liian vanha!")
        elif vuosi > 2021:
            print("Et ole vielä syntynyt!")
        else:
            lista.append((nimi, vuosi))
    except ValueError:
        print("Vuosi pitää antaa numeroina!")
