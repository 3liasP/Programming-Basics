nimi = input("Anna nimi: ")
ika = int(input("Anna ika: "))

if nimi == "":
    print("Et antanut nimeä")

if ika < 0:
    print("Et ole vielä syntynyt")

if ika > 130:
    print("En usko")

print("Kiitos!")