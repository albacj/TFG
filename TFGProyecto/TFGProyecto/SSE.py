import random
import math
import numpy as np

class SSE(object):
    
    def __init__(self, k, sek, d, w):
        self.k = k

    def ssKeyGen(k,p):
        sek = []

        # parámetros de seguridad, para definir el vector de 0s y 1s
        #k = k
        ls = random.randint(1,p) 
        ps = random.randint(1,p)

        # algoritmo de encriptación simétrico
        xi = []

        for i in range(ls):
            i = random.randint(0,1)
            xi.append(i)

        # tam texto plano
        lineas = []
        n = 0

        # abre archivo (y cierra cuando termine lectura)
        with open("C:/Users/Alba/Documents/TFG/ExampleText.txt") as fichero:
            # recorre línea a línea el archivo
            for linea in fichero:
                # muestra línea última leída
                lineas.append(linea)

        for l in lineas:
            num = len(l.split())
            n = n + num

        # permutaciones pseudo-aleatorias

        delta = []
        tau = []
        mi = []
        
        for i in range(ps):
            i = random.randint(0,1)
            delta.append(i)

        for i in range(int(math.log10(n))):
            i = random.randint(0,1)
            tau.append(i)

        for i in range(int(ls + ps + math.log10(n))):
            i = random.randint(0,1)
            mi.append(i)

        # función pseudoaleatoria
        
        f = []

        for i in range(int(ls + math.log10(n))):
            i = random.randint(0,1)
            f.append(i)

        # ssKeyGen
        oneK = [1 for i in range(k)]
        oneLs = [1 for i in range(ls)]

        # claves aleatorias

        uHut = random.randint(1,p)
        y = random.randint(1,p)
        z = random.randint(1,p)
        eta = random.randint(1,p)

        sek.append(uHut)
        sek.append(y)
        sek.append(z)
        sek.append(eta)
        sek.append(oneLs)

        return sek, delta, z, f, y, mi
    
#    def buildIndex(sek, d):
#        pass
#        #devuelve indice i

    def trapdoor(sek, wi, delta, z, f, y, mi):
        y = sek[1]
        z = sek[2]

        wordNum = []
        
        for letter in wi:
            wordNum.append(ord(letter))

        # asocio a wordNum un único número multiplicando sus elementos
        for num in wordNum:
            mul = 1
            mul = mul * num

        mulZ = mul * z

        # delta sub z
        deltaZ = []

        for i in delta:
            if(i == 1):
                deltaZ.append(mulZ)
            else:
                deltaZ.append(0)

        # función sub y
        fY = []
        mulY = mul * y

        for i in f:
            if(i == 1):
                fY.append(mulY)
            else:
                fY.append(0)

        # TW'i
        twPrimei = []
        twPrimei.append(deltaZ)
        twPrimei.append(fY)

        # mi y eta
        mulEta = []

        for elem in twPrimei:
            mulEta.append(np.dot(sek[3],elem))

        # TWi
        twi = []
        
        for i in mi:
            if(i == 1):
                twi.append(mulEta)
            else:
                twi.append(0)

        return twi

    def search(i,tw):
        pass
        #devuelve D(w) (d que contega w)