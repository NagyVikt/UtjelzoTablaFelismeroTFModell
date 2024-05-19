### Projekt README: Útjelző Táblák Felismerése OCR és TensorFlow Technológiával

#### Projekt Leírás
Ez a projekt egy innovatív Optikai Karakterfelismerő (OCR) algoritmus kifejlesztésére irányul, amely képes az útjelző táblák felismerésére és a rajtuk szereplő szöveges információk digitalizálására. A modern képfeldolgozási technikákat és gépi tanulási modelleket, mint például a TensorFlow-t alkalmazva elemzi a közlekedési jelzéseket, azonosítja a szimbólumokat és a szöveges utasításokat, támogatva ezzel a vezetők tájékozódását és döntéshozatalát. A projekt célja egy olyan GUI (grafikus felhasználói interfész) megalkotása, amely képes felismerni és azonosítani a beadott útjelző táblákat a feldolgozott 100 különböző típus közül.

#### Főbb Jellemzők
- Képfeldolgozás és gépi tanulás alapú szövegfelismerés
- TensorFlow segítségével tréningelt modell alkalmazása
- Interaktív GUI-n keresztüli tábla felismerés
- Támogatás többféle útjelző tábla azonosítására
- Pontos és megbízható szöveges és vizuális kimenet generálása

#### Előfeltételek
A projekt futtatásához szükséged lesz a következőkre:
- Python 3.6 vagy újabb
- TensorFlow 2.x
- OpenCV
- PIL (Pillow)
- NumPy
- Pandas
- Matplotlib (opcionális grafikonokhoz)

#### Telepítés
1. Klónozd a projekt GitHub repóját a helyi gépedre:
   ```bash
   git clone https://github.com/NagyVikt/OCRSZE.git
   ```
2. Lépj be a projekt könyvtárba:
   ```bash
   cd ocr-traffic-sign-recognition
   ```
3. Hozz létre egy virtuális környezetet:
   ```bash
   python -m venv venv
   ```
4. Aktiváld a virtuális környezetet:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS és Linux:
     ```bash
     source venv/bin/activate
     ```
5. Telepítsd a függőségeket:
   ```bash
   pip install -r requirements.txt
   ```

#### Használat
A GUI indításához futtasd a fő Python szkriptet a projekt gyökérkönyvtárában:
```bash
python main.py
```
A GUI-n keresztül töltheted fel az útjelző táblák képeit, amelyeket a rendszer elemz, és azonnali visszajelzést ad a felismerés eredményéről.

#### Fejlesztés
- A képek előfeldolgozása: Ez magában foglalja a méretezést, szürkeárnyalatos konverziót, és zajszűrést.
- Modell tréningelése és finomhangolása: Használj több különböző adathalmazt a modell robustusságának növelésére.
- GUI fejlesztése: Implementálj további funkciókat a felhasználói élmény javítása érdekében.

#### A modell betanítása során mért idő
A modell felépítése az adott képek számától függően körülbelül 15 percet vesz igénybe.

#### A modell betanítása során mért metrikákák jelentése
1. accuracy (Pontosság)
Jelentés: Az accuracy vagy pontosság azt mutatja meg, hogy a modell mennyire képes helyesen osztályozni az adatokat. %-os pontossággal képes helyesen azonosítani a tanító adatkészletben szereplő címkéket. Ha ez pl.0,43 az azt jelenti, hogy körülbelül 100 kérdésből átlagosan 43-at helyesen tud beazonosítani.
2. loss (Veszteség)
Jelentés: A loss vagy veszteség az a szám, ami azt mutatja, mennyire távol vannak a modell által előrejelzett értékek a valós címkéktől. A veszteség alacsonyabb értéke azt jelzi, hogy a modell jobban illeszkedik az adatokhoz.
3. val_accuracy (Validációs Pontosság)
Jelentés: A val_accuracy hasonló a fent említett accuracy-hoz, de ez a validációs adatkészletre vonatkozik. Ha ez magasabb, mint a tanító adatkészleten mért pontosság, az azt sugallja, hogy a modell jól teljesít az új, eddig nem látott adatokon. Ebben az esetben ez azt mutatja, hogy a modell általánosítási képessége jó.
4. val_loss (Validációs Veszteség)
Jelentés: A val_loss az a veszteség, amit a modell a validációs adatkészleten produkál. Ha ez az érték jelentősen alacsonyabb, mint a tanítási veszteség, az jó jel, mivel azt mutatja, hogy a modell hatékonyan képes generalizálni az új adatokra.



#### Közreműködés
Minden közreműködést szívesen fogadunk! Nyiss egy issue-t a javaslatoddal vagy hibajelentéssel, vagy küldj be egy pull requestet a változtatásokkal.




#### Licenc


#### Szerző
- Projekt készítője: Nagy Viktor

#### Referenciák
- [TensorFlow hivatalos weboldala](https://www.tensorflow.org/)
- [OpenCV dokumentáció](https://opencv.org/)
- [PIL (Pillow) dokumentáció](https://pillow.readthedocs.io/)
- [Pytesseract GitHub oldala](https://github.com/madmike/ocr-Template-matching)
- [GTSRB (German Traffic Sign Recognition Benchmark) dataset a Kaggle-on](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
- [Chinese Traffic Sign Database](https://nlpr.ia.ac.cn/pal/trafficdata/recognition.html)