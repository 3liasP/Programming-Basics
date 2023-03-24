from datetime import datetime

ika = input("Anna syntymäpäiväsi (esim 8.11.2001): ")

lista = ika.split(".")
bd_d = lista[0]
bd_m = lista[1]
bd_y = lista[2]
birthdate = datetime(int(bd_y), int(bd_m), int(bd_d))
age =  str(datetime.now() - birthdate)
toinen = age.split(" ")
paivat = toinen[0]
print(f"Olet nyt {paivat} päivää vanha.")
