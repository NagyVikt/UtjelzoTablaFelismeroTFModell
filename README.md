# Útjelző Táblák Felismerése Trensflow és OCR Technológiával

## Projekt Leírás

Ez a projekt egy olyan OCR (Optikai Karakterfelismerő) algoritmus kifejlesztésére irányul, amely képes az útjelző táblák felismerésére és a rajtuk szereplő szöveges információk digitalizálására. Az algoritmus a modern képfeldolgozási technikákat alkalmazva elemzi a közlekedési jelzéseket, azonosítja a szimbólumokat és a szöveges utasításokat, támogatva ezzel a vezetők tájékozódását és döntéshozatalát.

### Főbb Jellemzők

- Képfeldolgozás alapú szövegfelismerés
- Minták és szimbólumok felismerése (pl. STOP tábla)
- Támogatás többféle útjelző tábla azonosítására
- Pontos és megbízható szöveges kimenet generálása

## Kezdő lépések

### Előfeltételek

A projekt futtatásához szükséged lesz Pythonra, virtuális könyvtárra és néhány külső fájlra. 
Kövesd a következő lépéseket 


### Telepítés

1. Klónozd a repót:
```bash
git clone https://github.com/NagyVikt/OCRSZE.git
```

2. Telepítsd a függőségeket a lejebb megadott pip parancsokkal.


Virtuális Környezet Létrehozása
A projekt függőségeinek elkülönítése érdekében ajánlott egy virtuális környezet használata. Hozd létre és aktiváld a virtuális környezetet a következő parancsokkal:

Virtuális környezet létrehozása:

```bash
python -m venv venv
```
Virtuális környezet aktiválása:

Windows esetén:
```bash
.\venv\Scripts\activate
```
macOS és Linux esetén:
```bash
source venv/bin/activate
```
Függőségek telepítése a requirements.txt fájlból:

```bash
pip install -r requirements.txt
```

## Használat

Helyezd az útjelző tábla képeit egy mappába, és futtasd a fő scriptet a következő parancs segítségével:
```bash
python main.py --images_path ./your_image_folder_path
```
A script kimenete tartalmazni fogja a felismert táblákat és azok szöveges kimenetét.

## Fejlesztés

A projekt iteratív fejlesztése során a következő lépésekre van szükség:

1. Képek előfeldolgozása a jobb felismerés érdekében.
2. Minta felismerés és karakterfelismerés finomhangolása.
3. Tesztelés különböző környezeti feltételek mellett.
4. Teljesítmény javítása és optimalizálás.

## Főbb lépesek

1. Környezet Beállítása
Az általad megadott könyvtárak nagyon hasznosak lesznek a képfeldolgozás és a gépi tanulás területén, így az első lépésben telepítenünk kell ezeket. A numpy segít a tömbműveletekben, a matplotlib a vizualizációban, a scikit-learn a gépi tanulási modellekkel kapcsolatos munkában, a scikit-image a képfeldolgozásban, és az opencv-python (OpenCV) az egyik legnépszerűbb képfeldolgozó könyvtár, amelyet széles körben használnak OCR feladatokban is.

2. OCR és Minta Felismerés
Az OCR (Optikai Karakterfelismerés) technológia alkalmazásához a pytesseract könyvtárat is hozzáadtam, amely a Google Tesseract-OCR engine Python interfészét biztosítja. A Tesseract egyik legfejlettebb és legpontosabb ingyenes OCR motorja, amely több mint 100 nyelvet támogat.

3. Prototípus Fejlesztése
Kép előfeldolgozása: Az OCR pontosságának növelése érdekében először elő kell dolgozni a képeket. Ez magában foglalhat zajcsökkentést, szín- vagy fényerő normalizálást, élek kiemelését, stb.
Minta felismerés: Az útjelző táblákon lévő szimbólumok és minták felismerése fontos. Az OpenCV könyvtár funkcióit, mint a kontúrkeresés és a formafelismerés, használhatjuk a jellegzetes minták, pl. a STOP tábla nyolcszögletű formájának azonosítására.
Karakterfelismerés: A pytesseract használatával olvasd be a szöveges információt a táblákról. A karakterfelismerési folyamat finomhangolása érdekében használj speciális konfigurációs paramétereket, amelyek megkönnyítik az egyedi formátumú vagy stílusú szövegek felismerését.
Szöveg és minta összekapcsolása: Az olvasott szöveget és felismert mintákat összekapcsolva hozd létre a végleges outputot, ami a tábla által közvetített utasítás szöveges formában történő megjelenítése.

4. Tesztelés és Optimalizálás
Teszteld az algoritmust különböző típusú útjelző táblákkal, fényviszonyokkal és szögekkel. Gyűjts statisztikákat a pontosságról és a hibákról, és finomítsd az algoritmust a gyűjtött adatok alapján.
Optimalizáld a kód futási idejét és a felismerés pontosságát. Kísérletezz különböző előfeldolgozási technikákkal és paraméterbeállításokkal.


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


https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign?resource=download
https://www.analyticsvidhya.com/blog/2021/12/traffic-signs-recognition-using-cnn-and-keras-in-python/