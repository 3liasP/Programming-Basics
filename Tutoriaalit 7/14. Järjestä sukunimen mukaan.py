def jarjesta_sukunimen_mukaan(nimilista: list):
    nimilista.sort(key=lambda alkio: alkio.split(" ")[1])
    return nimilista