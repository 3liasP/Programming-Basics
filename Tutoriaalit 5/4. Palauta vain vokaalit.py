def vain_vokaalit(jono: str) -> str:
    table = str.maketrans(dict.fromkeys('dghjklmnprstv'))
    jono = jono.translate(table)
    return jono


print(vain_vokaalit("kalevi"))