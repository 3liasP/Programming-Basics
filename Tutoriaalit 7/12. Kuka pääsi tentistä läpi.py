def lapipaasseet(opiskelijat: list) -> list:
    return [tuppe[0] for tuppe in opiskelijat if tuppe[1] >= 50]