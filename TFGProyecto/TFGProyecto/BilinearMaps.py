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