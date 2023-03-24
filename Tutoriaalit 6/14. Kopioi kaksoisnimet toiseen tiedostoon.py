def kopioi_kaksoisnimet(lahde: str, kohde: str):
    with open(lahde) as tiedosto:
        with open (kohde, "w") as kopiot:
            for rivi in tiedosto:
                nimi = rivi.strip()
                if "-" in nimi:
                    kopiot.write(nimi + "\n")