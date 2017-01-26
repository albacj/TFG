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
        #return g
        for i in range(g):
            pass

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