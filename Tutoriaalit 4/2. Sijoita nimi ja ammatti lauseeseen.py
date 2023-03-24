def sijoita(lause, nimi, ammatti):

    if "ammatti" in lause:
        uusi = lause.replace("ammatti", ammatti)
    if "nimi" in lause:
        uusi = uusi.replace("nimi", nimi)

    print(uusi)


sijoita("Moi olen nimi ja ammatiltani ammatti.", "Pekka", "poliisi")