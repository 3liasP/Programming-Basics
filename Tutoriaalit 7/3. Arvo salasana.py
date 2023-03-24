import random

def arvo_salasana(pituus: int) -> str:
    lista = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    numerot = [1,2,3,4,5,6,7,8,9]
    isot = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    pienet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    x = 0
    salasana = ""
    salasana += str(random.choice(numerot))
    salasana += random.choice(isot)
    salasana += random.choice(pienet)

    while x < (pituus - 3):
        arvaus = str(random.choice(lista))
        if arvaus in salasana:
            pass
        else:
            salasana += arvaus
        x += 1

    salasana = ''.join(random.sample(salasana,len(salasana)))
    return salasana
    



print(arvo_salasana(10))