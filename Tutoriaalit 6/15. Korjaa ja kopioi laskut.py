def korjaa_ja_kopioi():
    with open("laskut.csv") as tiedosto:
        with open("korjatut_laskut.csv", "w") as kopio:
            for rivi in tiedosto:
                kokoLasku = str(rivi.strip())
                lasku = rivi.strip().split("=")
                if lasku[0][0].isnumeric() == False:
                    muutos = str(int(lasku[1]) - int(lasku[0][lasku[0].find("+")+1:]))
                    oikea = kokoLasku.replace(kokoLasku[:kokoLasku.find("+")], muutos)
                    kopio.write(f"{oikea}\n")
                elif lasku[0][lasku[0].find("+")+1:].isnumeric() == False:
                    muutos = str(int(lasku[1]) - int(lasku[0][0]))
                    oikea = kokoLasku.replace(kokoLasku[kokoLasku.find("+")+1:kokoLasku.find("=")], muutos)
                    kopio.write(f"{oikea}\n")
                else:
                    muutos = str(int(lasku[0][0]) + int(lasku[0][2]))
                    oikea = kokoLasku.replace(kokoLasku[kokoLasku.find("=")+1:], muutos)
                    kopio.write(f"{oikea}\n")