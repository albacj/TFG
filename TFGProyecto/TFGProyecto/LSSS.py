import BilinearMaps
import random
import numpy as np

from itertools import chain
from itertools import combinations
from sympy import Symbol

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
        setParties.pop(0)
            
        for x in setParties: #Las acciones de cada parte en P forman un vector sobre Zp. 1a condición

            if(list(x) <= BilinearMaps.BilinearMaps.zetaP(p)):
                condition1 = True
                continue

            maxList = max(setParties)
            maxTam = len(maxList)

        l = len(setParties)
        # n <= num elementos del array más grande de setParties para que salga una matriz cuadrada a lo sumo
        n = random.randint(1, maxTam) 
        shareGenerateMatrix = []
        rho = []
        v = []
        sBig = random.choice(setParties) # S elemento de setParties (A)
        j = []
        lambdaSub_i = []
        mv = []
        secret = Symbol('s') # el secreto que se comparte. Incógnita porque se va resolviendo (s en el documento)
        res = 0
        omega = []

        # matriz shareGenerateMatrix M
        for x in setParties:
            x = list(x)
            shareGenerateMatrix.append(x)

        for i in range(len(shareGenerateMatrix)):

            e = shareGenerateMatrix[i]
            
            if(len(e) > n):
                e = e[0:n]
                
            else:
                diff = n - len(e)
                e += [0] * diff

            shareGenerateMatrix[i] = e

        # preparando el vector v
        v.append(secret)

        for r in range(2,n+1):
            r = random.choice(BilinearMaps.BilinearMaps.zetaP(p))
            v.append(r)

        # vector resultante mv
        shareGenerateMatrix = np.reshape(shareGenerateMatrix, (len(shareGenerateMatrix), n))
        v = np.reshape(v, (n,1))
        mv = np.dot(shareGenerateMatrix, v)

        # rho de cada i, dato de curiosidad mencionado en el documento
        for i in mv:
            rho.append(i)

        # cálculo de lambda sub i para hallar s
        for i in shareGenerateMatrix:
            res = np.dot(i,v)
            lambdaSub_i.append(res)

        for i in range(l+1):
            j.append(i+1)

            for j in rho:
                if(j in sBig):
                    pass
            #if(i in sBig):

        # ya devolvemos un valor booleano que confirma (o no) si el esquema de compartición secreta es bilineal
        condition2 = True

        if((condition1 and condition2) == True):
            linear = True

        return linear