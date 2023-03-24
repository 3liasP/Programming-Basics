sana = input("Anna sana: ")

uusi = sana.replace("Å","A")
uusi = uusi.replace("å","a")
uusi = uusi.replace("Ä","A")
uusi = uusi.replace("ä","a")
uusi = uusi.replace("Ö","O")
uusi = uusi.replace("ö","o")

print("Ilman ääkkösiä:", uusi)