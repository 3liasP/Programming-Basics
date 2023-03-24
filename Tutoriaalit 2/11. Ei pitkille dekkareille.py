genre = input("Anna tyylilaji: ")
sivu = int(input("Anna sivumäärä: "))

if genre != "dekkari":
    print("Luetaan pois")

if genre == "dekkari" and sivu > 200:
    print("En jaksa lukea")

if genre == "dekkari" and sivu < 200:
    print("Luetaan pois")