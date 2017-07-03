class SSE(object):
    
    def __init__(self, k, sek, d, w):
        self.k = k

    def ssKeyGen(k):
        sek = []

        # parámetros de seguridad
        k = k
        #ls =
        #ps =

        # algoritmo de encriptación simétrico

        # tam texto plano
        
        fileText = open("C:/Users/Alba/Documents/TFG/ExampleText.txt", "r")
        content = fileText.read()
        
        for char in fileText:
            print(char)

        #fileText.close()

        return sek
    
    def buildIndex(sek, d):
        pass
        #devuelve indice i

    def trapdoor(sek, w):
        pass
        #devuelve tw

    def search(i,tw):
        pass
        #devuelve D(w) (d que contega w)