import numpy
import random

from random import randrange

class BilinearMaps(object):
    
    def __init__(self, p):
        self.p = p

    def zetaP(p):
        z = []
        for i in range(p-1):
            z.append(i+1)
        return list(z)

    #Genera ciclo de un número cualquiera
    def cyclic(p):
        g = BilinearMaps.zetaP(p)
        i = 1
        found = False

        while(i <= len(g) and not found):
            gCyclic = []
            generator = i
            
            for x in g:
                elem = (generator**x) % p

                if elem not in gCyclic:
                    gCyclic.append(elem)

            found = (len(gCyclic) == p-1)
            i = i+1

        return gCyclic

    #Problema de logaritmo discreto es infactible
    def notPLD(c1, c2):
        c1 = BilinearMaps.zetaP(p)
        c2 = BilinearMaps.cyclic(p)
        pass

    #Definicion de mapa bilineal de la misma dimension que el ciclo dado como entrada: G x G -> Gt
    def e(c1,c2,p):
        #return numpy.multiply(c, c)
        
        # si tiene que ser mod p:
        gt = numpy.multiply(c1,c2)
        gtSol = []

        for item in gt:
            item = item % p
            gtSol.append(item)

        return gtSol

    #Propiedades:

    def bilinear(p):

        satisfied = False
        pVBefore = []
        qVBefore = []

        g = BilinearMaps.zetaP(p)

        while(satisfied):

            a = g[random.randint(0,p-1)]
            b = g[random.randint(0,p-1)]

            i = random.randint(0,p-1)
            j = random.randint(0,p-1)
            pV = g[0: i]
            qV = g[0: j]

            for item in pV:
                pVBefore.append(item**a)

            for item in qV:
                qVBefore.append(item**b)

            resBefore = BilinearMaps.e(pVBefore, qVBefore, 11)

            resAfter = BilinearMaps.e(pV, qV, 11)
            resAfter = resAfter**(a*b)

            if(resBefore == resAfter):
                satisfied = True
            
        return satisfied

    def nonDegenerate():
        pass

    def computable():
        pass