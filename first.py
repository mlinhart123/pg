# Program pro zjištění, zda je číslo sudé nebo liché

# Zadej číslo
cislo = int(input("Zadej číslo: "))

# Kontrola, zda je číslo sudé nebo liché
if cislo % 2 == 0:
    print(f"{cislo} je sudé číslo.")
else:
    print(f"{cislo} je liché číslo.")
