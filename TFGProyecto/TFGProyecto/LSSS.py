import BilinearMaps
import random
import numpy as np

from itertools import chain
from itertools import combinations

class LSSS(object):

    def __init__(self,c):
        self.c = c

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
    def lsss(c):
        linear = False

        setParties = list(chain.from_iterable(combinations(c, r) for r in range(len(c)+1)))
        setParties.sort(key = len)
        
        def productIsLinear(setParties):
            
            for x in setParties: #Las acciones de cada parte en P forman un vector sobre Zp.
                pass
            if():
                l = len(setParties)
                shareGenerateMatrix = np.empty((l,n))