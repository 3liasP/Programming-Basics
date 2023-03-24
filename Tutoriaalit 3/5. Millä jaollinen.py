luku = int(input("Anna luku: "))

jakaja = 1

while jakaja <= luku:

    if luku % jakaja == 0:
        print(luku, "on jaollinen luvulla", jakaja)
    
    jakaja += 1