import BilinearMaps
import random

class LSSS(object):

    def __init__(self):
        pass

    #Definicion 1
    def accessStructure(c):

        def isEven(x):
            return x % 2 == 0
        
        def powerPack(c): #conjunto potencia
            n = len(c)

            # crear lista con 2^n conjuntos vacios
            subsets = []
            for i in range(2 ** n):
                subsets.append(list())

            # convierto a lista para poder ir recorriendo los elementos por su indice i
            elements = list(c)

            for i in range(n):
                x = elements[i]
                for j in range(2 ** n):
                    if isEven(j / (2 ** i)):
                        subsets[j].append(x)

            subsets2 = []
            for i in subsets:
                if i not in subsets2:
                    subsets2.append(i)

            subsets2 = sorted(subsets2)
            return subsets2
        
        parties = powerPack(c)

        # posible tam de a
        i = random.randint(1,len(parties))
        
        # coleccion a
        a = random.sample(parties,i)

        def isMonotone(a):
            monotone = False
            
            j = random.randint(1,len(parties))
            k = random.randint(1,len(parties))

            b = random.sample(parties,j)
            c = random.sample(parties,k)

            while(not monotone):
                if((b in a) and (b in c)):
                    if(c in a):
                        monotone = True

            return monotone

        isTrue = isMonotone(a)
        print(isTrue)

    #Definicion 2
    def lsss():
        pass

