alku = int(input("Anna alku: "))
loppu = int(input("Anna loppu: "))

summa = [alku]

while alku < loppu:
    alku = alku + 1
    summa.append(alku)

print("Summa on", sum(summa))