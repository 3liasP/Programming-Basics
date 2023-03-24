
summa = 0

while True:
    luku = int(input("Anna luku: "))
    summa = summa + luku
    if luku == 0:
        print("Lukujen summa on", summa)
        break