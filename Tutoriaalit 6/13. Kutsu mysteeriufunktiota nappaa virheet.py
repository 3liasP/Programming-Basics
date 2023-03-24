def mysteerifunktio(arvo):
    return int(arvo)

try:
    print(f"Funktio palautti luvun {mysteerifunktio()}")
except ValueError:
    print("Tuli ValueError!")
except ZeroDivisionError:
    print("Tuli ZeroDivisionError!")
except TypeError:
    print("Tuli TypeError!")

