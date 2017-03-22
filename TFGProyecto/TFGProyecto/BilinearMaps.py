import numpy
import random
import numbers

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

        return gCyclic, generator

    #Definicion de mapa bilineal de la misma dimension que el ciclo dado como entrada: G x G -> Gt
    def e(c1,c2):
        
        #tiene que ser mod p, además de ser un vector:
        if(c1 is list and len(c1) > 1):
            gt = numpy.multiply(c1,c2)
            gtSol = []

            for item in gt:
                item = item % (len(gt)+1) # len + 1 es p
                gtSol.append(item)

            return gtSol

        else:
            return numpy.multiply(c1,c2)

    #Propiedades:

    def bilinear(c):
        satisfied = False

        while(not satisfied):

            # a y b son dos numeros aleatorios
            a = random.randint(1,len(c))
            b = random.randint(1,len(c))

            # elementos aleatorios de c
            p = random.choice(c)
            q = random.choice(c)

            pElevate = (p**a)
            qElevate = (q**b)

            eBefore = BilinearMaps.e(pElevate,qElevate)
            eProvisional = BilinearMaps.e(p,q)
            eAfter = eProvisional**(a*b)

            if(eBefore == eAfter and eBefore != 0):
                satisfied = True
                
        print(eBefore, eAfter)
        return satisfied

    def nonDegenerate(c):
        satisfied = False

        while(not satisfied):
            p = random.choice(c)
            eP = BilinearMaps.e(p,p)

            if(eP != 1):
                satisfied = True

        print(eP)
        return satisfied