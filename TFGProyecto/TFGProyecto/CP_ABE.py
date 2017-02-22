import BilinearMaps
import _random

class CP_ABE(object):
    
    def __init__(self, phi, u, s, message, structureA):
        self.phi = phi
        self.u = u
        self.s = s
        self.message = message
        self.structureA = structureA

    def phiFunction(n): #n es un numero dado
        
        def isPrime(a):
            return not ( a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))

        y = n

        for i in range(2,n+1):
            if isPrime(i) and n % i == 0:
                y = y * (1 - 1/i)

        return int(y)

    def setup(phi,u): #u es un número
       pass

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