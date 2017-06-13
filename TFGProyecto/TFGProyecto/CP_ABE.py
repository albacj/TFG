import BilinearMaps
import random

class CP_ABE(object):
    
    def __init__(self, phi, u, s, message, structureA, n, p):
        self.phi = phi
        self.u = u
        self.s = s
        self.message = message
        self.structureA = structureA
        self.n = n
        self.p = p

    def phiFunction(n): #n es un numero dado
        
        def isPrime(a):
            return not (a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))

        y = n

        for i in range(2,n+1):
            if isPrime(i) and n % i == 0:
                y = y * (1 - 1/i)

        return int(y)

    def setup(phi,u,p): # u es el número de usuarios
       pk = []
       msk = 0
       gElevateA = 0
       eMapElevate = []

       group, g = BilinearMaps.BilinearMaps.cyclic(p)
       eMap = BilinearMaps.BilinearMaps.e(group, group)

       def isOk(group):
           ok = False

           #Si el G cumple las propiedades bilineales y no degenerativas
           if((BilinearMaps.BilinearMaps.bilinear(group) and BilinearMaps.BilinearMaps.nonDegenerate(group)) == True):
               ok = True

           return ok

       if(isOk(group) == True):
           alpha = random.choice(BilinearMaps.BilinearMaps.zetaP(p))
           a = random.choice(BilinearMaps.BilinearMaps.zetaP(p))

           h = []
           i = 0

           while(i < u):
               h.append(random.choice(group))
               i = i + 1
            
           msk = g ** alpha

           for elem in eMap:
               eMapElevate.append(elem ** alpha)

           gElevateA = g ** a

           pk.append(group)
           pk.append(g)
           pk.append(eMapElevate)
           pk.append(g ** a)
           pk.append(h)

       return pk, msk, gElevateA, h   

    def keyGen(msk,h,p, gElevateA):
        sk = []
        k = 0
        l = 0
        t = 0
        kSubx = []

        group, g = BilinearMaps.BilinearMaps.cyclic(p)
        t = random.choice(BilinearMaps.BilinearMaps.zetaP(p))

        k = msk * (gElevateA** t)
        l = g ** t

        for x in h: # h es el conjunto de atributos S
            kSubx.append(x ** t)

        sk.append(k)
        sk.append(l)
        sk.append(kSubx)

        return sk

    def encrypt(pk,message,structureA):
        pass
        #devuelve ct

    def decrypt(pk,sk,ct):
        pass
        #devuelve message