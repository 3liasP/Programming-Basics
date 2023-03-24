def jarjesta_tuloksen_mukaan(opiskelijat: list):
    opiskelijat.sort(key=lambda alkio: max(alkio[1], alkio[2], alkio[3]))
    return opiskelijat