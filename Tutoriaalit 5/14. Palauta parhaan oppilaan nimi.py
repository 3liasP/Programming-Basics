keskiarvot = {"Paula": 5.5, "Heikki": 7.75, "Aapeli": 9.25, "Tiina": 7.5, "Pate": 6.5, "Arto": 9.0, "Hilkka": 8.25, "Aune": 6.25, "Timo": 4.5}

def paras_keskiarvo(keskiarvot: dict) -> int:
    key_list = list(keskiarvot.keys())
    val_list = list(keskiarvot.values())

    paras_ka = max(val_list)
    position = val_list.index(paras_ka)
    return (key_list[position])

paras_keskiarvo(keskiarvot)