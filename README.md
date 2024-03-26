

# Útjelző Táblák Felismerése TensorFlow és OCR Technológiával

## Projekt Leírás

Ez a projekt egy olyan OCR (Optikai Karakterfelismerő) algoritmus kifejlesztésére irányul, amely képes az útjelző táblák felismerésére és a rajtuk szereplő szöveges információk digitalizálására. Az algoritmus a modern képfeldolgozási technikákat és gépi tanulási modelleket, mint például a TensorFlow-t alkalmazva elemzi a közlekedési jelzéseket, azonosítja a szimbólumokat és a szöveges utasításokat, támogatva ezzel a vezetők tájékozódását és döntéshozatalát.

E projekt különlegessége, hogy a TensorFlow segítségével létrehozott modellt képek alapján tréningeljük, amelyek az útjelző táblákat ábrázolják. A projekt célja egy olyan GUI (grafikus felhasználói interfész) megalkotása, amely képes felismerni és azonosítani a beadott útjelző táblákat a feldolgozott 100 különböző típus közül.

### Főbb Jellemzők

- Képfeldolgozás és gépi tanulás alapú szövegfelismerés
- TensorFlow segítségével tréningelt modell alkalmazása
- GUI-n keresztüli interaktív tábla felismerés
- Támogatás többféle útjelző tábla azonosítására
- Pontos és megbízható szöveges és vizuális kimenet generálása

## Kezdő lépések

### Előfeltételek

A projekt futtatásához szükséged lesz Pythonra, TensorFlow-ra, egy virtuális könyvtárra és néhány külső fájlra. A pontos előfeltételeket és a telepítési útmutatót az alábbiakban találod.

### Telepítés

[Telepítési lépések ismertetése, beleértve a TensorFlow és más függőségek telepítését.]

## Használat

[Útmutató a GUI használatához, beleértve, hogy hogyan kell betölteni a képeket és hogyan történik az útjelző táblák felismerése.]

## Fejlesztés

[Leírás a projekt iteratív fejlesztési lépéseiről, beleértve a képek előfeldolgozását, a modell tréningelését és finomhangolását, valamint a GUI fejlesztését.]

## Főbb lépések

[A projekt főbb lépéseinek részletes ismertetése, többek között a TensorFlow modell építése, tréningelése és tesztelése, valamint a GUI integrációja.]

## Közreműködés

Minden közreműködést szívesen fogadunk! Nyiss egy issue-t a javaslatoddal vagy hibajelentéssel, vagy küldj be egy pull requestet a változtatásokkal.

## Licenc

Ez a projekt [MIT licenc](LICENSE.txt) alatt áll.

## Szerző

- Projekt készítője: Nagy Viktor

## Referenciák

- [Pytesseract GitHub oldala](https://github.com/madm

Referenciák

- [TensorFlow hivatalos weboldala](https://www.tensorflow.org/)
- [Scikit-image dokumentáció](https://scikit-image.org/docs/dev/index.html)
- [OpenCV dokumentáció](https://opencv.org/)
- [UJjelző tablák képei](https://www.szuperjogsi.hu/)
- [GTSRB (German Traffic Sign Recognition Benchmark) dataset a Kaggle-on](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign?resource=download)
- [Traffic Signs Recognition Using CNN and Keras](https://www.analyticsvidhya.com/blog/2021/12/traffic-signs-recognition-using-cnn-and-keras-in-python/)

A projekt az útjelző táblák felismeréséhez és azonosításához képfeldolgozási technikákat és gépi tanulást használ. A TensorFlow és más releváns technológiák, mint a pytesseract (OCR), OpenCV (képfeldolgozás), és scikit-image (képelemzés) alkalmazásával egy olyan rendszert hozunk létre, ami képes az útjelző táblák széles skálájának felismerésére. A GUI-n keresztül történő interakció lehetővé teszi a felhasználók számára, hogy egyszerűen feltölthessék a táblák képeit, melyeket a rendszer elemz, és azonnali visszajelzést ad a felismerés eredményéről.

### Környezet beállítása

A sikeres projektindításhoz szükség van a megfelelő környezet előkészítésére, amely magában foglalja a TensorFlow, a pytesseract, az OpenCV és egyéb függőségek telepítését. Ezek a könyvtárak biztosítják a szükséges alapokat a képek előfeldolgozásához, a modell építéséhez és tréningeléséhez, valamint az OCR funkciókhoz.

### Tesztelés és optimalizálás

A rendszer tesztelése és optimalizálása kulcsfontosságú lépés a projekt fejlesztési ciklusában. Szükséges a különböző típusú útjelző táblákkal, fényviszonyokkal és szögekkel való tesztelés, hogy növeljük a rendszer adaptivitását és megbízhatóságát. Az adatgyűjtés és -elemzés segít a rendszer finomhangolásában, hogy a lehető legpontosabb és leggyorsabb eredményeket érjük el.

### GUI fejlesztése

A felhasználóbarát interfész megtervezése és implementálása fontos a projekt sikeréhez. A GUI-nak intuitívnak kell lennie, lehetővé téve a felhasználók számára, hogy könnyen navigáljanak, feltölthessék a képeket és gyorsan megkapják a felismerési eredményeket.

Ez a projekt olyan technológiai megoldásokat alkalmaz, amelyek előremozdítják a gépi tanulás és a képfeldolgozás területét, különös tekintettel az útjelző táblák felismerésére. A projekt célja, hogy növelje a közúti biztonságot azzal, hogy digitális eszközökkel támogatja a vezetők tájékozódását és döntéshozatalát.