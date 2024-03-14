# OCRSZE
Útjelző táblák olvasása és értelmezése OCR segítségével

A projekt célja egy olyan OCR algoritmus kifejlesztése, amely képes az utjelző táblák felismerésére és szöveges információjuk digitalizálására. A rendszer olyan képfeldolgozási technikákat fog alkalmazni, melyek révén elemezni tudja a közlekedési jelzéseket, azonosítani tudja a szimbólumokat és a szöveges utasításokat, ezáltal támogatva a vezetők tájékozódását és döntéshozatalát. 
Az OCR algoritmus nem csupán a szövegelemzésre, hanem minták alapján történő felismerésre is képes lesz, mint például a "STOP" tábla esetében, ahol a karakterfelismerés mellett a vizuális minta is számít. Az algoritmus képes lesz a táblákon lévő utasítások pontos és megbízható értelmezésére és azoknak egyértelmű szöveges kimenet formájában való megjelenítésére. 

Input: egy útjelző tábla képe.
Output: a hozzá tartozó megfelelő utasítás kiírása. 

Step 1: Environment Setup

pip install numpy matplotlib scikit-learn scikit-image opencv-python
