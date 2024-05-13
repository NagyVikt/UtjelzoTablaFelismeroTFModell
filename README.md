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
   git clone https://github.com/[your-github-username]/ocr-traffic-sign-recognition.git
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