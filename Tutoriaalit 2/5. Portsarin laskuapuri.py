synt = int(input("Anna syntymävuosi: "))
nyk = int(input("Anna nykyinen vuosi: "))

if nyk - synt >= 18:
    print("Tervetuloa")
else:
    print("Et ole tarpeeksi vanha.")