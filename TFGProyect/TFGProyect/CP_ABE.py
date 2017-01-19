import BilinearMaps
import _random

class CP_ABE(object):
    
    def __init__(self, phi, u, s, message, structureA):
        self.phi = phi
        self.u = u
        self.s = s
        self.message = message
        self.structureA = structureA

    def setup(phi,u): #u es un número
        pk = list()
        h = []
        #llamar a la función de mapa bilineal
        while(u>0):
            h.append(_random.Random(g)) #un g que hay de antes
            u = u-1
        h.sort()
        a = _random.Random(BilinearMaps.BilinearMaps.zetaP(p))
        alpha = _random.Random(BilinearMaps.BilinearMaps.zetaP(p))
        
        #actualización de valores
        pk.append(g)
        pk.append(gen)
        pk.append(BilinearMaps.BilinearMaps.e(gen,gen)**alpha)
        pk.append(gen**a)
        pk.append(h)
        msk = gen**alpha

        #devuelve pk y msk
        return pk, msk
        

    def keyGen(msk,s):
        pass
        #devuelve sk

    def encrypt(pk,message,structureA):
        pass
        #devuelve ct

    def decrypt(pk,sk,ct):
        pass
        #devuelve message (no es un parametro derivado)