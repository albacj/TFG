import numpy

class BilinearMaps(object):
    
    def __init__(self, p, g, gt):
        self.p = p
        self.g = []
        self.gt = []

    def zetaP(p):
        z = []
        for i in range(p-1):
            z.append(i+1)
        return list(z)

    def cyclic(p):
        g = BilinearMaps.zetaP(p)
        i = 1
        while(i <= len(g)):
            gCyclic = []
            alpha = i

            for x in g:
                gCyclic.append((alpha**x) % p)
            
            for elem in gCyclic: #si todos los elementos del ciclo son distintos entre ellos, ciclo válido
                pass

            i = i+1
            print("Ciclo con generador " + str(i-1) + ": " + str(gCyclic))

    def notPLD():
        pass

    def e(elem1, elem2):
        pass

    def bilinear():
        pass

    def nonDegenerate():
        pass

    def computable():
        pass