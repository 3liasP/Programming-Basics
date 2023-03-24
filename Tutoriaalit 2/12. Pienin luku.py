eka = int(input("Anna 1. luku: "))
toka = int(input("Anna 2. luku: "))
kolmas = int(input("Anna 3. luku: "))

if eka < toka and eka < kolmas:
    print("Luku 1 oli pienin")

if toka < eka and toka < kolmas:
    print("Luku 2 oli pienin")

if kolmas < toka and kolmas < eka:
    print("Luku 3 oli pienin")
