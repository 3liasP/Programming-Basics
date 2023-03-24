import random


rc = random.choice

etunimet = "Pekka Pirjo Paula Arto Kimmo Liisa Maija Lasse Leena".split()
sukunimet = "Virtanen Lahtinen Hakanen Järvinen Jokinen Saarinen".split()

etunimi = rc(etunimet)
sukunimi = rc(sukunimet)
ika = random.randint(10,99)

print("Moi, nimeni on", etunimi, sukunimi, "ja olen", ika, "vuotta vanha.")