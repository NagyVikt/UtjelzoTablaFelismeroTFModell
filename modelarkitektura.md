Konvolúciós rétegek (Conv2D)
Magyarázat: 
A konvolúciós réteg (Conv2D) a konvolúciós neurális hálózatok (CNN) egyik alapvető építőeleme. A konvolúciós rétegek kulcsfontosságúak a képfeldolgozási és mintafelismerési feladatokban, mert lehetővé teszik a modellek számára, hogy hatékonyan kinyerjék a bemeneti adatok (például képek) jellemzőit. Részletesen nézzük meg, mit jelent a konvolúciós réteg és hogyan működik:

Konvolúciós Réteg Feladata és Működése
Szűrők (Filtek) és Kernels:

A konvolúciós rétegek szűrőket (vagy kernelt) használnak a bemeneti adatok feldolgozására. Ezek a szűrők általában kisebbek, mint a bemeneti kép, például 3x3 vagy 5x5 méretűek. Egy konvolúciós réteg több ilyen szűrőt használ.
Konvolúciós Művelet:

A konvolúciós művelet során a szűrő végigcsúszik (konvolválódik) a bemeneti képen. Minden pozícióban a szűrő és a kép egy részének elemi szorzatait összegzi, és ez az érték kerül a kimeneti térbe. Ezt az eljárást csúszó ablaknak vagy más néven felcsévélésnek is nevezik.
Kimeneti Alak (Output Shape):

A kimeneti tér (feature map) mérete a szűrő méretétől, a lépésköztől (stride), és az esetleges padding-től függ. Például, ha a bemeneti kép 28x28 pixel méretű, egy 3x3-as szűrővel és 1-es lépésközzel dolgozunk, akkor a kimeneti tér mérete 26x26 lesz.
Receptív Mező:

A receptív mező az a bemeneti adat részhalmaza, amely egy adott kimeneti neuront befolyásol. A szűrő méretétől függően a receptív mező lehet nagyobb vagy kisebb


conv2d (Conv2D):

Szűrők száma: 32
Szűrő mérete: 5x5
Kimeneti alak: (None, 26, 26, 32)
Funkció: A konvolúciós rétegek feladata a képek különböző jellemzőinek (például élek, textúrák) kinyerése. Az első konvolúciós réteg 32 szűrőt használ, mindegyik 5x5 méretű. Ezek a szűrők a bemeneti képen végigcsúszva detektálnak különböző jellemzőket. Az eredmény egy 26x26 méretű térbeli kimenet, amely 32 csatornát tartalmaz (egy-egy csatorna minden egyes szűrő kimenete).
conv2d_1 (Conv2D):

Szűrők száma: 32
Szűrő mérete: 5x5
Kimeneti alak: (None, 22, 22, 32)
Funkció: A második konvolúciós réteg tovább finomítja az első réteg által kinyert jellemzőket. A kimeneti alak kisebb, mert a konvolúciós művelet során a szélek mentén történő átfedések miatt a térbeli méret csökken.
Max Pooling rétegek (MaxPooling2D)
max_pooling2d (MaxPooling2D):
Pooling ablak mérete: 2x2
Kimeneti alak: (None, 11, 11, 32)
Funkció: A max pooling rétegek csökkentik a térbeli méreteket, miközben megőrzik a legfontosabb jellemzőket. A pooling ablak 2x2 méretű, ami azt jelenti, hogy a bemeneti képből 2x2-es blokkokon belül a maximális értéket veszi figyelembe. Ez a művelet segít csökkenteni a számítási terhelést és a hálózat méretét.
Dropout rétegek (Dropout)
dropout (Dropout):
Arány: 25%
Kimeneti alak: (None, 11, 11, 32)
Funkció: A dropout réteg véletlenszerűen kinullázza a bemenet egyes elemeit az overfitting* csökkentése érdekében. A 25%-os dropout azt jelenti, hogy minden bemeneti elem 25%-os valószínűséggel kinullázódik. Ez segít megelőzni, hogy a hálózat túlzottan alkalmazkodjon a tanító adatokhoz, így jobban általánosíthat a teszt adatokon.

*Az overfitting (túltanulás) egy gyakori probléma a gépi tanulásban és a mélytanulási modellekben, amikor egy modell túl jól illeszkedik a tanító adatokhoz, de nem tud jól általánosítani a még nem látott, új adatokon. Az overfitting során a modell megtanul minden apró részletet és zajt a tanító adatokban, ami azt eredményezi, hogy túlzottan specifikus lesz ezekre az adatokra. Emiatt, amikor új adatokat kap, nem tudja jól teljesíteni a feladatát.

Az overfitting jelei a következők lehetnek:

Nagyon alacsony hiba a tanító adatokon, de magas hiba a teszt adatokon:

Ha a modell teljesítménye sokkal jobb a tanító adatokon, mint a teszt adatokon, az overfittingre utalhat.
Komplex modell:

A túl komplex modellek (például nagyon sok réteggel és neuronnal rendelkező hálózatok) hajlamosak az overfittingre, mert túl sok paraméterük van, ami lehetővé teszi számukra, hogy túlzottan pontosan illeszkedjenek a tanító adatokra.

További konvolúciós rétegek
conv2d_2 (Conv2D):

Szűrők száma: 64
Szűrő mérete: 3x3
Kimeneti alak: (None, 9, 9, 64)
Funkció: A harmadik konvolúciós réteg mélyebb jellemzőket tanul a bemenetből, mivel több szűrőt használ (64) és kisebb méretűek a szűrők (3x3). Ez a réteg finomabb részleteket és összetettebb jellemzőket képes kinyerni.
conv2d_3 (Conv2D):

Szűrők száma: 64
Szűrő mérete: 3x3
Kimeneti alak: (None, 7, 7, 64)
Funkció: A negyedik konvolúciós réteg tovább mélyíti a jellemzők tanulását. Az újabb konvolúciós műveletek további csökkenést eredményeznek a térbeli méretben, de növelik a jellemzők komplexitását.
Max Pooling és Dropout rétegek
max_pooling2d_1 (MaxPooling2D):

Pooling ablak mérete: 2x2
Kimeneti alak: (None, 3, 3, 64)
Funkció: A második max pooling réteg ismét csökkenti a térbeli méretet, ezúttal 3x3-ra, miközben megtartja a legfontosabb jellemzőket.
dropout_1 (Dropout):

Arány: 25%
Kimeneti alak: (None, 3, 3, 64)
Funkció: A második dropout réteg tovább csökkenti az overfitting lehetőségét a jellemző térben, véletlenszerűen kinullázva a bemenetek 25%-át.
Flatten réteg
flatten (Flatten):
Kimeneti alak: (None, 576)
Funkció: A flatten réteg a térbeli jellemzőtérből (3x3x64) egy egydimenziós vektort készít. Ez a vektor tartalmazza az összes kinyert jellemzőt, amelyet a sűrű rétegek használnak fel a végső osztályozáshoz.
Sűrű rétegek (Dense)
dense (Dense):

Neuronszám: 256
Aktivációs függvény: ReLU (Rectified Linear Unit)
Kimeneti alak: (None, 256)
Funkció: A sűrű réteg teljesen összekapcsolja a bemenetet az egyes neuronokkal. A ReLU aktivációs függvény non-linearitást ad a modellnek, ami segít a komplex jellemzők tanulásában.
dropout_2 (Dropout):

Arány: 50%
Kimeneti alak: (None, 256)
Funkció: Ez a dropout réteg 50%-os arányban kinullázza a bemenet elemeit, tovább csökkentve az overfitting lehetőségét.
dense_1 (Dense):

Neuronszám: 43
Aktivációs függvény: Softmax
Kimeneti alak: (None, 43)
Funkció: A végső sűrű réteg 43 neuront tartalmaz, ami az osztályok számával egyenlő. A softmax aktivációs függvény az egyes osztályok valószínűségét számítja ki, lehetővé téve a bemenet osztályozását.
Összefoglalás
Ez a CNN architektúra jól illeszkedik képfeldolgozási feladatokhoz, például képosztályozáshoz. Az egyes rétegek speciális feladatokat látnak el: a konvolúciós rétegek jellemzőket nyernek ki, a max pooling rétegek csökkentik a térbeli méreteket, a dropout rétegek csökkentik az overfitting lehetőségét, a flatten réteg átalakítja a térbeli jellemzőket egy dimenziójú vektorrá, a sűrű rétegek pedig elvégzik az osztályozást. Ez az architektúra biztosítja, hogy a modell képes legyen jól általánosítani új, ismeretlen képeken is.






