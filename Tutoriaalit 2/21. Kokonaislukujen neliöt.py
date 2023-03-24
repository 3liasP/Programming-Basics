limit = int(input("Anna yläraja: "))
kerroin = 0

while True:
    
    summa = (kerroin + 1) * (kerroin + 1)
    if summa >= limit:
        break
    
    print((kerroin + 1),"*",(kerroin + 1),"=",(kerroin + 1) * (kerroin + 1))

    kerroin = kerroin + 1