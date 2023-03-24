hinta = int(input("Anna lipun hinta: "))
ika = int(input("Anna ikä: "))

if ika < 12:
    print("Hinnaksi tuli", hinta * 0.5, "euroa.")
elif ika > 63:
    print("Hinnaksi tuli", hinta * 0.25, "euroa.")
else:
    print("Hinnaksi tuli", hinta * 0.95, "euroa.")