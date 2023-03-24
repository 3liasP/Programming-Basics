from datetime import datetime

def tulosta_aika(aika: datetime):
    paiva = str(aika.day)
    kuukausi = str(aika.month)
    tunti = str(aika.hour)
    minuutti = str(aika.minute)
    if len(kuukausi) == 1:
        kuukausi = f"0{aika.month}"
    if len(minuutti) == 1:
        minuutti = f"0{aika.minute}"
    if len(tunti) == 1:
        tunti = f"0{aika.hour}"
    if len(paiva) == 1:
        paiva = f"0{aika.day}"
    print("Muistan sen kuin eilisen päivän.")
    print(f"Vuosi oli {aika.year}, päivämäärä {paiva}.{kuukausi}.")
    print(f"Kello oli tasan {tunti}:{minuutti}.")

tulosta_aika(datetime.now)