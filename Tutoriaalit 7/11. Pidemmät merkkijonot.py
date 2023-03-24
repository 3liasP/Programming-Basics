def pidemmat_jonot(merkkijonot: list, raja: int) -> list:
    return [alkio for alkio in merkkijonot if len(alkio) > raja]