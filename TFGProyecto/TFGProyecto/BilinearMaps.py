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

        return gCyclic #, generator

    #Problema de logaritmo discreto es infactible
    def notPLD(c1, c2):
        c1 = BilinearMaps.cyclic(p)
        c2 = BilinearMaps.cyclic(p)
        pass

    #Definicion de mapa bilineal de la misma dimension que el ciclo dado como entrada: G x G -> Gt
    def e(c1,c2):
        #return numpy.multiply(c1, c2) # si tiene que ser un vector
        return numpy.inner(c1,c2)
        
        # si tiene que ser mod p, además de ser un vector:
        #gt = numpy.multiply(c1,c2)
        #gtSol = []

        #for item in gt:
        #    item = item % (len(gt)+1) # len + 1 es p
        #    gtSol.append(item)

        #return gtSol

    #Propiedades:

    def bilinear(c):
        satisfied = False

        while(not satisfied):

            # a y b son dos numeros aleatorios
            a = random.randint(1,len(c)+1)
            b = random.randint(1,len(c)+1)

            # k es el tam del subconjunto
            k = random.randint(1,len(c))

            # subconjuntos aleatorios de c
            p = random.sample(c,k)
            q = random.sample(c,k)

            pElevate = []
            qElevate = []

            for x in p:
                pElevate.append(x**a)

            for x in q:
                qElevate.append(x**b)

            eBefore = BilinearMaps.e(pElevate,qElevate)
            eProvisional = BilinearMaps.e(p,q)
            eAfter = eProvisional**(a*b)

            if(eBefore == eAfter):
                satisfied = True

        print(eBefore, eAfter)
        return satisfied

    def nonDegenerate(c):
        satisfied = False

        while(not satisfied):
            k = random.randint(0,len(c))
            p = random.sample(c,k)
            eP = BilinearMaps.e(p,p)

            if(eP != 1):
                satisfied = True

        print(eP)
        return satisfied

    def computable():
        pass

    # Miscelánea
    def cyclicGen(p):
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

        return generator #, generator