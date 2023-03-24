merkit = 1

yhdys = ""

while True:
    sana = input("Anna sana: ")

    yhdys += sana
    
    if len(yhdys) >= 20:
        print("Yhdyssanaksi tuli:", yhdys)
        break