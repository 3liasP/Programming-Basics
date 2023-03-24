raha = int(input("Kuinka paljon käytit rahaa? "))
#Bonukset:

if 0 <= raha <= 99:
    print(raha, "eurolla saa 10 bonuspistettä!")
elif 100 <= raha <= 499:
    print(raha, "eurolla saa 30 bonuspistettä!")
elif 500 <= raha <= 999:
    print(raha, "eurolla saa 50 bonuspistettä!")
elif 1000 <= raha <= 4999:
    print(raha, "eurolla saa 100 bonuspistettä!")
elif raha > 5000:
    print(raha, "eurolla saa 150 bonuspistettä!")