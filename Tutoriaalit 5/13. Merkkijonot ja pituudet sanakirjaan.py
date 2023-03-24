sanakirja = {}

while True:
    jono = input("Anna jono, tyhjä lopettaa: ")
    if jono == "":
        break
    pituus = len(jono)
    sanakirja[jono] = (pituus)

print(f"Sanakirja: {sanakirja}")