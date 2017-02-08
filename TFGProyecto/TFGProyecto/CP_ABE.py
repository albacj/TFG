import BilinearMaps
import _random

class CP_ABE(object):
    
    def __init__(self, phi, u, s, message, structureA):
        self.phi = phi
        self.u = u
        self.s = s
        self.message = message
        self.structureA = structureA

    def phiFunction(n):
        pass #http://blog.hackxcrack.net/introduccion-a-la-criptografia-moderna-con-python-2-rsa/

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