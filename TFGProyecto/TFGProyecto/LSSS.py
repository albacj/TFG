import BilinearMaps
import random
import numpy as np

from itertools import chain
from itertools import combinations

class LSSS(object):

    def __init__(self,c,p):
        self.c = c
        self.p = p

    #Definicion 1
    def accessStructure(c):

        def powerSet(s):
            return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
        
        parties = powerSet(c)

        # posible tam de a (A subconjunto de las partes)
        i = random.randint(0,len(parties))
        
        # coleccion a
        setA = random.sample(parties,i)
        setB = ()
        setC = ()

        def isMonotone(setA):
            monotone = False
            
            while(monotone == False):
                k = random.randint(0,len(setA)) # tam y coleccion c
                setC = random.sample(parties,k)

                setB = list(random.choice(parties)) # b es un elemento aleatorio de las partes

                # si b in a y b <= c entonces c in a
                if(not((setB in setA) and (setB <= setC)) or (setC in setA)):
                    monotone = True
                break

            return monotone

        return isMonotone(setA), parties, setA, setB, setC, len(parties)

    #Definicion 2
    def lsss(c,p):

        linear = False
        condition1 = False
        condition2 = False

        setParties = list(chain.from_iterable(combinations(c, r) for r in range(len(c)+1)))
        setParties.sort(key = len)
            
        for x in setParties: #Las acciones de cada parte en P forman un vector sobre Zp. 1a condición

            if(x <= BilinearMaps.BilinearMaps.zetaP(c)):
                condition1 = True
                continue

            maxTam = max(len(x))

        l = len(setParties)
        # n <= num elementos del array más grande de setParties para que salga una matriz cuadrada a lo sumo
        n = random.randint(1, maxTam) 
        #shareGenerateMatrix = np.empty((l,n))
        shareGenerateMatrix = []
        rho = []
        v = []
        j = []
        sBig = random.choice(setParties)
        secret = 0

        for x in setParties:
            x = list(x)
            if(len(x) > n):
                x = x[0:n-1]

            for i in range(l):
                rho[i+1] = x
                shareGenerateMatrix.append(rho[i+1])

        for i in range(l+1):
            j.append(i+1)


        v.append(secret)

        for r in range(2, n+1):
            r = random.randint(BilinearMaps.BilinearMaps.zetaP(p))
            v.append(r)

        condition2 = True

        if((condition1 and condition2) == True):
            linear = True

        return linear, shareGenerateMatrix