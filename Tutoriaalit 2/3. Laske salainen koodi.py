ekaluku = int(input("Anna eka luku: "))
tokaluku = int(input("Anna toka luku: "))

yht = (ekaluku + tokaluku)

if yht % 2 != 0:
    print("Koodi on:", yht * 5)

if yht % 2 == 0:
    print("Koodi on:", yht * 10)