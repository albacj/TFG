import numpy

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
    def notPLD():
        pass

    #Definicion de mapa bilineal de la misma dimension que el ciclo dado como entrada
    def e(c,p):
        #return numpy.multiply(c, c)
        
        # si tiene que ser mod p:
        gt = numpy.multiply(c,c)
        gtSol = []

        for item in gt:
            item = item % p
            gtSol.append(item)

        return gtSol


    #Propiedades:

    def bilinear():
        pass

    def nonDegenerate():
        pass

    def computable():
        pass