leveys = int(input("Anna leveys: "))
korkeus = int(input("Anna korkeus: "))

laskuri = 1

print("*" * leveys)

while laskuri < korkeus - 1:
    lev = "*" * leveys
    vali = leveys - 4
    print("*", vali * " " ,"*")
    laskuri += 1


print("*" * leveys)