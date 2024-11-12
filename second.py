# cislo na text 

jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
specialni_desitky = ["", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
stovky = ["", "sto", "dvě stě", "tři sta", "čtyři sta", "pět set", "šest set", "sedm set", "osm set", "devět set"]

def cislo_text(cislo):
    if cislo == 0:
        return "nula"
    
    vysledek = ""

    if cislo >= 100:
        vysledek += stovky[cislo // 100] + " "
        cislo %= 100

    if 10 < cislo < 20:
        vysledek += specialni_desitky[cislo - 10]
    else:
        if cislo >= 10:
            vysledek += desitky[cislo // 10] + " "
        cislo %= 10

        if cislo > 0:
            vysledek += jednotky[cislo]

    return vysledek.strip()

cislo = int(input("Zadej číslo: "))

textova_podoba = cislo_na_text(cislo)

print(textova_podoba)

