def tulosta_fibot(n):
    # ekat kaksi
    n1, n2 = 1, 1
    index = 1
    while index <= n:
        print(n1)
        nth = n1 + n2
        # uudet arvot
        n1 = n2
        n2 = nth
        index += 1

tulosta_fibot(6)