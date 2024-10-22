# prvocislo true nebo false

import math
def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, int(math.sqrt(cislo)) + 1):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla
  
if __name__ == "__main__":
    cislo = int(input("Zadej číslo pro kkontrolu prvočísla: "))
    if je_prvocislo(cislo):
        print(f"{cislo}: True")
    else:
        print(f"{cislo}: False")
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(f"Prvočísla mezi 1 a {maximum}: {prvocisla}")
