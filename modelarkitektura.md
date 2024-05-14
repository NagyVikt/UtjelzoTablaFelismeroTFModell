Ez az ábra egy konvolúciós neurális hálózat (CNN) architektúráját mutatja be, amelyet képfeldolgozási feladatokra, például képosztályozásra használnak. Az egyes dobozok a hálózat rétegeit ábrázolják, és mindegyik réteg alatt az adott réteg kimeneti alakját (output shape) láthatjuk. Nézzük meg részletesebben az egyes rétegeket:

conv2d (Conv2D):

Első konvolúciós réteg, amely 32 szűrőt használ, mindegyik szűrő 5x5 méretű.
Kimeneti alak: (None, 26, 26, 32)
None az első dimenzió a batch size-ot jelöli, amely nem meghatározott.
26, 26 a térbeli dimenziókat jelöli (magasság, szélesség).
32 a szűrők száma, ami a kimeneti csatornák számával egyenlő.
conv2d_1 (Conv2D):

Második konvolúciós réteg, szintén 32 szűrőt használ, mindegyik szűrő 5x5 méretű.
Kimeneti alak: (None, 22, 22, 32)
max_pooling2d (MaxPooling2D):

Max pooling réteg, amely 2x2 méretű pooling ablakot használ.
Kimeneti alak: (None, 11, 11, 32)
dropout (Dropout):

Dropout réteg, amely 25%-os arányban véletlenszerűen kinullázza a bemenet egyes elemeit az overfitting csökkentése érdekében.
Kimeneti alak: (None, 11, 11, 32)
conv2d_2 (Conv2D):

Harmadik konvolúciós réteg, 64 szűrőt használ, mindegyik szűrő 3x3 méretű.
Kimeneti alak: (None, 9, 9, 64)
conv2d_3 (Conv2D):

Negyedik konvolúciós réteg, szintén 64 szűrőt használ, mindegyik szűrő 3x3 méretű.
Kimeneti alak: (None, 7, 7, 64)
max_pooling2d_1 (MaxPooling2D):

Második max pooling réteg, amely 2x2 méretű pooling ablakot használ.
Kimeneti alak: (None, 3, 3, 64)
dropout_1 (Dropout):

Dropout réteg, amely 25%-os arányban véletlenszerűen kinullázza a bemenet egyes elemeit az overfitting csökkentése érdekében.
Kimeneti alak: (None, 3, 3, 64)
flatten (Flatten):

Flatten réteg, amely egy 1D vektorba lapítja a bemenetet.
Kimeneti alak: (None, 576)
Ez az érték a 3x3x64 = 576 szorzat eredménye.
dense (Dense):

Fully connected (sűrű) réteg, amely 256 neuront tartalmaz és relu aktivációs függvényt használ.
Kimeneti alak: (None, 256)
dropout_2 (Dropout):

Dropout réteg, amely 50%-os arányban véletlenszerűen kinullázza a bemenet egyes elemeit az overfitting csökkentése érdekében.
Kimeneti alak: (None, 256)
dense_1 (Dense):

Kimeneti fully connected réteg, amely 43 neuront tartalmaz (az osztályok száma).
Kimeneti alak: (None, 43)
A softmax aktivációs függvényt használja a valószínűségek kiszámításához minden osztályra.
Ez a hálózat arra van tervezve, hogy képekből (például közlekedési táblák) jellemzőket tanuljon és azokat megfelelő osztályokba sorolja. Az egyes rétegek specifikus feladatokat látnak el a képek jellemzőinek kinyerésében és feldolgozásában, végül pedig a sűrű rétegek segítségével az osztályozást végzik el.






