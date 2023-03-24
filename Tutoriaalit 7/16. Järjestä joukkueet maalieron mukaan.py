def jarjesta_maalieron_mukaan(joukkueet: list):
    def maaliero(t:tuple):
        luvut = t[1].split("-")
        ero = int(luvut[0]) - int(luvut[1])
        return ero
    joukkueet.sort(key=maaliero)
    return joukkueet