def poista_vokaalit(sana: str) -> str:
    table = str.maketrans(dict.fromkeys('aeiouyåäö'))
    sana = sana.translate(table)
    return sana

print(poista_vokaalit("äiti"))