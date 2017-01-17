class CP_ABE(object):
    
    def __init__(self, phi, u, s, message, structureA):
        self.phi = phi
        self.u = u
        self.s = s
        self.message = message
        self.structureA = structureA

    def setup(phi,u):
        pass
        #devuelve pk y msk

    def keyGen(msk,s):
        pass
        #devuelve sk

    def encrypt(pk,message,structureA):
        pass
        #devuelve ct

    def decrypt(pk,sk,ct):
        pass
        #devuelve message (no es un parametro derivado)