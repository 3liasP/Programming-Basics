kolmosia = 0
summa = 0
maara = 0

while True:
    intluku = int(input("Anna luku: "))
    if intluku == -1:
        break
    strluku = str(intluku)

    if "3" in strluku:
        maara = strluku.count("3")
        kolmosia += maara
    
    summa += intluku

print(f"Kolmosia: {kolmosia}")
print(f"Summa: {summa}")
