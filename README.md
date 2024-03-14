# Útjelző Táblák Felismerése OCR Technológiával

## Projekt Leírás

Ez a projekt egy olyan OCR (Optikai Karakterfelismerő) algoritmus kifejlesztésére irányul, amely képes az útjelző táblák felismerésére és a rajtuk szereplő szöveges információk digitalizálására. Az algoritmus a modern képfeldolgozási technikákat alkalmazva elemzi a közlekedési jelzéseket, azonosítja a szimbólumokat és a szöveges utasításokat, támogatva ezzel a vezetők tájékozódását és döntéshozatalát.

### Főbb Jellemzők

- Képfeldolgozás alapú szövegfelismerés
- Minták és szimbólumok felismerése (pl. STOP tábla)
- Támogatás többféle útjelző tábla azonosítására
- Pontos és megbízható szöveges kimenet generálása

## Kezdő lépések

### Előfeltételek

A projekt futtatásához szükséged lesz Pythonra és néhány külső könyvtárra. Telepítsd ezeket a következő parancsokkal:

pip install numpy matplotlib scikit-learn scikit-image opencv-python pytesseract


### Telepítés

1. Klónozd a repót:

git clone https://github.com/NagyVikt/OCRSZE.git


2. Telepítsd a függőségeket a fent megadott pip parancsokkal.

## Használat

Helyezd az útjelző tábla képeit egy mappába, és futtasd a fő scriptet a következő parancs segítségével:

python main.py --images_path ./your_image_folder_path

A script kimenete tartalmazni fogja a felismert táblákat és azok szöveges kimenetét.

## Fejlesztés

A projekt iteratív fejlesztése során a következő lépésekre van szükség:

1. Képek előfeldolgozása a jobb felismerés érdekében.
2. Minta felismerés és karakterfelismerés finomhangolása.
3. Tesztelés különböző környezeti feltételek mellett.
4. Teljesítmény javítása és optimalizálás.

## Közreműködés

Minden közreműködést szívesen fogadunk! Nyiss egy issue-t a javaslatoddal vagy hibajelentéssel, vagy küldj be egy pull requestet a változtatásokkal.

## Licenc

Ez a projekt [MIT licenc](LICENSE.txt) alatt áll.

## Szerző
- Projekt készítője: Nagy Viktor

## Referenciák

- [OpenCV dokumentáció](https://docs.opencv.org/master/)
- [Pytesseract GitHub oldala](https://github.com/madmaze/pytesseract)
- [Scikit-image dokumentáció](https://scikit-image.org/docs/dev/index.html)
- [UJjelző tablak kepei](https://www.szuperjogsi.hu/)
