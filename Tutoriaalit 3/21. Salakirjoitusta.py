def salakirjoita(teksti):
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = "".join([abc[(abc.find(c)+13)%26] for c in teksti])
    print(secret)

salakirjoita("auto")
