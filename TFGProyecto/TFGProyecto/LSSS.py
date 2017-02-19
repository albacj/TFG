import BilinearMaps
import random

from itertools import chain
from itertools import combinations

class LSSS(object):

    def __init__(self):
        pass

    #Definicion 1
    def accessStructure(c):

        def powerSet(s):
            return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
        
        parties = powerSet(c)

        # posible tam de a
        i = random.randint(0,len(parties))
        
        # coleccion a
        a = random.sample(parties,i)

        def isMonotone(a):
            monotone = False
            
            while(not monotone):
                k = random.randint(0,len(a)) # tam y coleccion c
                c = random.sample(a,k)

                j = random.randint(0,len(c)) # tam y coleccion b
                b = random.sample(c,j)

                if(set(b) <= set(a) and set(b) <= set(c)):
                    if(set(c) <= set(a)):
                        monotone = True

            return monotone

        isTrue = isMonotone(a)
        
        def withoutEmpty(a):
            for x in a:
                if x == set():
                    a.remove(x)
            return a

        return a

    #Definicion 2
    def lsss():
        pass

