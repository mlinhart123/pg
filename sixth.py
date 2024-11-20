import sys
import requests
from bs4 import BeautifulSoup

def stahni_url_a_ziskej_vsechny_href(url):
    
    try:
        odpoved = requests.get(url) 
        if odpoved.status_code == 200:
            soup = BeautifulSoup(odpoved.content, "html.parser")
            odkazy = [odkaz.get("href") for odkaz in soup.find_all("a")]
            return odkazy
        else:
            return []  
    except requests.exceptions.RequestException as chyba:
        print(f"Chyba při stahování URL: {chyba}")
        return []

if __name__ == "__main__":
    try:
    
        url = sys.argv[1]
        vsechny_odkazy = stahni_url_a_ziskej_vsechny_href(url)
        
        if vsechny_odkazy:
            print("Odkazy:")  
            for odkaz in vsechny_odkazy:
                if odkaz:  
                    print(odkaz)
        else:
            print("Žádné odkazy nebyly nalezeny.")
    except IndexError:
        print("Zadejte prosím URL jako parametr při spuštění programu.")
    except Exception as chyba:
        print(f"Program skončil chybou: {chyba}")
