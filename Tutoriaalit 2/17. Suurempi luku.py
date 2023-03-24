while True:
    luku1 = int(input("Anna luku 1: "))
    luku2 = int(input("Anna luku 2: "))
    if luku1 == luku2:
        print("Kiitos!")
        break
    if luku1 > luku2:
        print(luku1, "oli suurempi!")
    if luku1 < luku2:
        print(luku2, "oli suurempi!")