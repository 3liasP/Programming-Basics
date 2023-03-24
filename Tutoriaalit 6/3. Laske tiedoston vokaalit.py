def laske_vokaalit(tiedostonimi: str) -> int:
    with open(tiedostonimi) as tiedosto:
        sisalto = tiedosto.read()
    vokaalit = sisalto.count("a") + sisalto.count("e") + sisalto.count("i") + sisalto.count("o") + sisalto.count("u") + sisalto.count("y") + sisalto.count("å") + sisalto.count("ä") + sisalto.count("ö") + sisalto.count("A") + sisalto.count("E") + sisalto.count("I") + sisalto.count("O") + sisalto.count("U") + sisalto.count("Y") + sisalto.count("Å") + sisalto.count("Ä") + sisalto.count("Ö")
    return vokaalit