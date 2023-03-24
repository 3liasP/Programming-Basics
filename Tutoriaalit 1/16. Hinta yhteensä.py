#ALKUPERÄINEN KOODI NÄYTTI TÄLTÄ:

#kpl = int(input("Anna kappalemäärä: "))
#hinta = int(input("Anna hinta: "))
#alennus = int(input("Anna alennus%: "))
#alekerroin = (1-alennus/100)
#print("Hinta yhteensä: ", ((kpl*hinta)*alekerroin))


#UUSI KOODI JOONAKSELTA:

kpl = int(input("Anna kappalemäärä: "))
hinta = float(input("Anna hinta: "))
alennus = int(input("Anna alennus%: "))

kok_hinta = (1 - (alennus/100))*(kpl*hinta)

if kpl == 3:
    print("Hinta yhteensä:", round(kok_hinta, 2))
else:
    print("Hinta yhteensä:", round(kok_hinta, 1))