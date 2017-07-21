import random
import math

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
                #print(linea)
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

        return sek
    
    def buildIndex(sek, d):
        pass
        #devuelve indice i

    def trapdoor(sek, w):
        pass
        #devuelve tw

    def search(i,tw):
        pass
        #devuelve D(w) (d que contega w)