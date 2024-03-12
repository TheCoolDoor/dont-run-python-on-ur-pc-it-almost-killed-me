import requests
from PIL import Image
from io import BytesIO

def kep_megjelenites(fizikus_neve):
    GOOGLE_IMAGE_API_URL = "https://www.googleapis.com/customsearch/v1"
    API_KEY = "YOUR_API_KEY"  # helyettesítsd be a saját API kulcsoddal
    CX = "YOUR_CX"  # helyettesítsd be a saját keresési azonosítóddal
    search_query = fizikus_neve + " fizikus"

    params = {
        "key": API_KEY,
        "cx": CX,
        "q": search_query,
        "searchType": "image",
        "num": 1  # Csak egy képet kérünk le
    }

    response = requests.get(GOOGLE_IMAGE_API_URL, params=params)
    data = response.json()

    if "items" in data and data["items"]:
        image_url = data["items"][0]["link"]
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        img.show()
    else:
        print("Nincs kép a megadott fizikusról.")
def beolvasas(fajlnev):
    adatok = []
    with open(fajlnev, 'r', encoding='utf-8') as file:
        file.readline()
        for sor in file:
            sor = sor.strip().split(';')
            sor[2] = int(sor[2])
            adatok.append(sor)
        
    return adatok

def lista_kiiras(adatok):
    for sor in adatok:
        print("Fizikus:", sor[0])
        print("Felfedezés:", sor[1])
        print("Évszám:", sor[2])
        print("Fenntarthatósági ágak:", sor[3])
        print()


def evszamok(adatok):
    evszam_lista = [sor[2] for sor in adatok]
    legkorabbi = min(evszam_lista)
    legkesobb = max(evszam_lista)
    atlag = sum(evszam_lista) / len(evszam_lista)
    print("Legkorábbi felfedezés évszáma:", legkorabbi)
    print("Legkésőbbi felfedezés évszáma:", legkesobb)
    print("Átlagos felfedezési évszám:", atlag)

def fizikus_kereses(adatok, fizikus_neve):
    for sor in adatok:
        if sor[0] == fizikus_neve:
            print("Fizikus:", sor[0])
            print("Felfedezés:", sor[1])
            print("Évszám:", sor[2])
            return
    print("Nem található adat ehhez a fizikushoz.")

def main():
    adatok = []
    while True:
        print("\nMenü:")
        print("1. Beolvasás")
        print("2. Adatok listázása")
        print("3. Legkorábbi, legkésőbbi és átlagos évszám")
        print("4. Fizikus keresése")
        print("5. Fizikus képének megjelenítése")
        print("0. Kilépés")

        valasztas = input("Válassz egy menüpontot: ")

        if valasztas == '1':
            fajlnev = input("Add meg a fájl nevét: ")
            adatok = beolvasas(fajlnev)
            print("Az adatok beolvasva.")

        elif valasztas == '2':
            if adatok:
                lista_kiiras(adatok)
            else:
                print("Nincsenek még beolvasott adatok.")

        elif valasztas == '3':
            if adatok:
                evszamok(adatok)
            else:
                print("Nincsenek még beolvasott adatok.")

        elif valasztas == '4':
            if adatok:
                fizikus_neve = input("Add meg a fizikus nevét: ")
                fizikus_kereses(adatok, fizikus_neve)
            else:
                print("Nincsenek még beolvasott adatok.")

        elif valasztas == '5':
            if adatok:
                fizikus_neve = input("Add meg a fizikus nevét: ")
                kep_megjelenites(fizikus_neve)
            else:
                print("Nincsenek még beolvasott adatok.")

        elif valasztas == '0':
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérlek, válassz a megadott lehetőségek közül.")


if __name__ == "__main__":
    main()


