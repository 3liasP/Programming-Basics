def tulosta_elokuva(nimi: str, ohjaaja: str, kesto: float, ikaraja: int, ohjelmistossa: bool):
    format_kesto = "{:.2f}".format(kesto)
    print(f"Elokuvasuositus: {nimi}, jonka ohjasi maineikas {ohjaaja}.")
    print(f"Elokuva kestää {format_kesto} minuuttia, ja sen ikäraja on {ikaraja}.")
    if ohjelmistossa == True:
        print("Elokuva on tällä hetkellä ohjelmistossa.")
    else:
        print("Elokuva ei ole tällä hetkellä ohjelmistossa.")

tulosta_elokuva("Rambo", "Scorese", 120.5, 18, False)