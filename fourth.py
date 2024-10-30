def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    typ = figurka["typ"]
    pozice = figurka["pozice"]
    
    x1, y1 = pozice
    x2, y2 = cilova_pozice
    
    if not (1 <= x2 <= 8 and 1 <= y2 <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "král":
        return abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1
    
    elif typ == "dáma":
        return x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1)
    
    elif typ == "střelec":
        return abs(x2 - x1) == abs(y2 - y1)
    
    elif typ == "věž":
        return x1 == x2 or y1 == y2
    
    elif typ == "jezdec":
        return (abs(x2 - x1), abs(y2 - y1)) in [(2, 1), (1, 2)]
    
    elif typ == "pěšec":
        if y2 == y1 + 1 and x1 == x2 and cilova_pozice not in obsazene_pozice:
            return True
        elif y2 == y1 + 1 and abs(x2 - x1) == 1 and cilova_pozice in obsazene_pozice:
            return True
        elif y1 == 2 and y2 == 4 and x1 == x2 and (x2, y2) not in obsazene_pozice:
            return True
        return False

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
