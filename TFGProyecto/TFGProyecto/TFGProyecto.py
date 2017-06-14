import BilinearMaps
import LSSS
import CP_ABE

ciclo1, generador1= BilinearMaps.BilinearMaps.cyclic(11)
ciclo2, generador2 = BilinearMaps.BilinearMaps.cyclic(7)

print("Ciclo 1: ")
print(ciclo1, generador1)

"""
Ciclo 1:
[2, 4, 8, 5, 10, 9, 7, 3, 6, 1] generador: 2
"""

print("\n")

print("Ciclo 2: ")
print(ciclo2, generador2)

'''
Ciclo 2:
[3, 2, 6, 4, 5, 1] generador: 3
'''

print("\n")

print("G x G -> Gt1: ")
print(BilinearMaps.BilinearMaps.e(ciclo1, ciclo1))

'''
G x G -> Gt1:
[  4  16  64  25 100  81  49   9  36   1]
'''

print("\n")

print("G x G -> Gt2: ")
print(BilinearMaps.BilinearMaps.e(ciclo2, ciclo2))

'''
G x G -> Gt2:
[ 9  4 36 16 25  1]
'''

print("\n")

print("Propiedad bilineal: ")
print(BilinearMaps.BilinearMaps.bilinear(ciclo1))

'''
Propiedad bilineal:
65536 65536
True
'''

print("\n")

print("Propiedad no degenerativa: ")
print(BilinearMaps.BilinearMaps.nonDegenerate(ciclo1))

'''
Propiedad no degenerativa:
64
True
'''

print("\n")

print("Access structure: ")
print(LSSS.LSSS.accessStructure(ciclo1))

'''
Access structure:
(True, [(), (2,), (4,), (8,), (5,), (10,), (9,), (7,), (3,), (6,), (1,), 
(2, 4), (2, 8), (2, 5), (2, 10), (2, 9), (2, 7), (2, 3), (2, 6), (2, 1), 
(4, 8), (4, 5), (4, 10), (4, 9), (4, 7), (4, 3), (4, 6), (4, 1), 
(8, 5), (8, 10), (8, 9), (8, 7), (8, 3), (8, 6), (8, 1), 
(5, 10), (5, 9), (5, 7), (5, 3), (5, 6), (5, 1), 
(10, 9), (10, 7), (10, 3), (10, 6), (10, 1), 
(9, 7), (9, 3), (9, 6), (9, 1), 
(7, 3), (7, 6), (7, 1), 
(3, 6), (3, 1), 
(6, 1), 
(2, 4, 8), (2, 4, 5), (2, 4, 10), (2, 4, 9), (2, 4, 7), (2, 4, 3), (2, 4, 6), (2, 4, 1), (2, 8, 5), (2, 8, 10), (2, 8, 9), (2, 8, 7), (2, 8, 3), (2, 8, 6), (2, 8, 1), (2, 5, 10), (2, 5, 9), (2, 5, 7), (2, 5, 3), (2, 5, 6), (2, 5, 1), (2, 10, 9), (2, 10, 7), (2, 10, 3), (2, 10, 6), (2, 10, 1), (2, 9, 7), (2, 9, 3), (2, 9, 6), (2, 9, 1), (2, 7, 3), (2, 7, 6), (2, 7, 1), (2, 3, 6), (2, 3, 1), (2, 6, 1), 
(4, 8, 5), (4, 8, 10), (4, 8, 9), (4, 8, 7), (4, 8, 3), (4, 8, 6), (4, 8, 1), (4, 5, 10), (4, 5, 9), (4, 5, 7), (4, 5, 3), (4, 5, 6), (4, 5, 1), (4, 10, 9), (4, 10, 7), (4, 10, 3), (4, 10, 6), (4, 10, 1), (4, 9, 7), (4, 9, 3), (4, 9, 6), (4, 9, 1), (4, 7, 3), (4, 7, 6), (4, 7, 1), (4, 3, 6), (4, 3, 1), (4, 6, 1), 
(8, 5, 10), (8, 5, 9), (8, 5, 7), (8, 5, 3), (8, 5, 6), (8, 5, 1), (8, 10, 9), (8, 10, 7), (8, 10, 3), (8, 10, 6), (8, 10, 1), (8, 9, 7), (8, 9, 3), (8, 9, 6), (8, 9, 1), (8, 7, 3), (8, 7, 6), (8, 7, 1), (8, 3, 6), (8, 3, 1), (8, 6, 1), 
(5, 10, 9), (5, 10, 7), (5, 10, 3), (5, 10, 6), (5, 10, 1), (5, 9, 7), (5, 9, 3), (5, 9, 6), (5, 9, 1), (5, 7, 3), (5, 7, 6), (5, 7, 1), (5, 3, 6), (5, 3, 1), (5, 6, 1), 
(10, 9, 7), (10, 9, 3), (10, 9, 6), (10, 9, 1), (10, 7, 3), (10, 7, 6), (10, 7, 1), (10, 3, 6), (10, 3, 1), (10, 6, 1), 
(9, 7, 3), (9, 7, 6), (9, 7, 1), (9, 3, 6), (9, 3, 1), (9, 6, 1), 
(7, 3, 6), (7, 3, 1), (7, 6, 1), 
(3, 6, 1), 
(2, 4, 8, 5), (2, 4, 8, 10), (2, 4, 8, 9), (2, 4, 8, 7), (2, 4, 8, 3), (2, 4, 8, 6), (2, 4, 8, 1), (2, 4, 5, 10), (2, 4, 5, 9), (2, 4, 5, 7), (2, 4, 5, 3), (2, 4, 5, 6), (2, 4, 5, 1), (2, 4, 10, 9), (2, 4, 10, 7), (2, 4, 10, 3), (2, 4, 10, 6), (2, 4, 10, 1), (2, 4, 9, 7), (2, 4, 9, 3), (2, 4, 9, 6), (2, 4, 9, 1), (2, 4, 7, 3), (2, 4, 7, 6), (2, 4, 7, 1), (2, 4, 3, 6), (2, 4, 3, 1), (2, 4, 6, 1), (2, 8, 5, 10), (2, 8, 5, 9), (2, 8, 5, 7), (2, 8, 5, 3), (2, 8, 5, 6), (2, 8, 5, 1), (2, 8, 10, 9), (2, 8, 10, 7), (2, 8, 10, 3), (2, 8, 10, 6), (2, 8, 10, 1), (2, 8, 9, 7), (2, 8, 9, 3), (2, 8, 9, 6), (2, 8, 9, 1), (2, 8, 7, 3), (2, 8, 7, 6), (2, 8, 7, 1), (2, 8, 3, 6), (2, 8, 3, 1), (2, 8, 6, 1), (2, 5, 10, 9), (2, 5, 10, 7), (2, 5, 10, 3), (2, 5, 10, 6), (2, 5, 10, 1), (2, 5, 9, 7), (2, 5, 9, 3), (2, 5, 9, 6), (2, 5, 9, 1), (2, 5, 7, 3), (2, 5, 7, 6), (2, 5, 7, 1), (2, 5, 3, 6), (2, 5, 3, 1), (2, 5, 6, 1), (2, 10, 9, 7), (2, 10, 9, 3), (2, 10, 9, 6), (2, 10, 9, 1), (2, 10, 7, 3), (2, 10, 7, 6), (2, 10, 7, 1), (2, 10, 3, 6), (2, 10, 3, 1), (2, 10, 6, 1), (2, 9, 7, 3), (2, 9, 7, 6), (2, 9, 7, 1), (2, 9, 3, 6), (2, 9, 3, 1), (2, 9, 6, 1), (2, 7, 3, 6), (2, 7, 3, 1), (2, 7, 6, 1), (2, 3, 6, 1), 
(4, 8, 5, 10), (4, 8, 5, 9), (4, 8, 5, 7), (4, 8, 5, 3), (4, 8, 5, 6), (4, 8, 5, 1), (4, 8, 10, 9), (4, 8, 10, 7), (4, 8, 10, 3), (4, 8, 10, 6), (4, 8, 10, 1), (4, 8, 9, 7), (4, 8, 9, 3), (4, 8, 9, 6), (4, 8, 9, 1), (4, 8, 7, 3), (4, 8, 7, 6), (4, 8, 7, 1), (4, 8, 3, 6), (4, 8, 3, 1), (4, 8, 6, 1), (4, 5, 10, 9), (4, 5, 10, 7), (4, 5, 10, 3), (4, 5, 10, 6), (4, 5, 10, 1), (4, 5, 9, 7), (4, 5, 9, 3), (4, 5, 9, 6), (4, 5, 9, 1), (4, 5, 7, 3), (4, 5, 7, 6), (4, 5, 7, 1), (4, 5, 3, 6), (4, 5, 3, 1), (4, 5, 6, 1), (4, 10, 9, 7), (4, 10, 9, 3), (4, 10, 9, 6), (4, 10, 9, 1), (4, 10, 7, 3), (4, 10, 7, 6), (4, 10, 7, 1), (4, 10, 3, 6), (4, 10, 3, 1), (4, 10, 6, 1), (4, 9, 7, 3), (4, 9, 7, 6), (4, 9, 7, 1), (4, 9, 3, 6), (4, 9, 3, 1), (4, 9, 6, 1), (4, 7, 3, 6), (4, 7, 3, 1), (4, 7, 6, 1), (4, 3, 6, 1), 
(8, 5, 10, 9), (8, 5, 10, 7), (8, 5, 10, 3), (8, 5, 10, 6), (8, 5, 10, 1), (8, 5, 9, 7), (8, 5, 9, 3), (8, 5, 9, 6), (8, 5, 9, 1), (8, 5, 7, 3), (8, 5, 7, 6), (8, 5, 7, 1), (8, 5, 3, 6), (8, 5, 3, 1), (8, 5, 6, 1), (8, 10, 9, 7), (8, 10, 9, 3), (8, 10, 9, 6), (8, 10, 9, 1), (8, 10, 7, 3), (8, 10, 7, 6), (8, 10, 7, 1), (8, 10, 3, 6), (8, 10, 3, 1), (8, 10, 6, 1), (8, 9, 7, 3), (8, 9, 7, 6), (8, 9, 7, 1), (8, 9, 3, 6), (8, 9, 3, 1), (8, 9, 6, 1), (8, 7, 3, 6), (8, 7, 3, 1), (8, 7, 6, 1), (8, 3, 6, 1), 
(5, 10, 9, 7), (5, 10, 9, 3), (5, 10, 9, 6), (5, 10, 9, 1), (5, 10, 7, 3), (5, 10, 7, 6), (5, 10, 7, 1), (5, 10, 3, 6), (5, 10, 3, 1), (5, 10, 6, 1), (5, 9, 7, 3), (5, 9, 7, 6), (5, 9, 7, 1), (5, 9, 3, 6), (5, 9, 3, 1), (5, 9, 6, 1), (5, 7, 3, 6), (5, 7, 3, 1), (5, 7, 6, 1), (5, 3, 6, 1), 
(10, 9, 7, 3), (10, 9, 7, 6), (10, 9, 7, 1), (10, 9, 3, 6), (10, 9, 3, 1), (10, 9, 6, 1), (10, 7, 3, 6), (10, 7, 3, 1), (10, 7, 6, 1), (10, 3, 6, 1), 
(9, 7, 3, 6), (9, 7, 3, 1), (9, 7, 6, 1), (9, 3, 6, 1), 
(7, 3, 6, 1), 
(2, 4, 8, 5, 10), (2, 4, 8, 5, 9), (2, 4, 8, 5, 7), (2, 4, 8, 5, 3), (2, 4, 8, 5, 6), (2, 4, 8, 5, 1), (2, 4, 8, 10, 9), (2, 4, 8, 10, 7), (2, 4, 8, 10, 3), (2, 4, 8, 10, 6), (2, 4, 8, 10, 1), (2, 4, 8, 9, 7), (2, 4, 8, 9, 3), (2, 4, 8, 9, 6), (2, 4, 8, 9, 1), (2, 4, 8, 7, 3), (2, 4, 8, 7, 6), (2, 4, 8, 7, 1), (2, 4, 8, 3, 6), (2, 4, 8, 3, 1), (2, 4, 8, 6, 1), (2, 4, 5, 10, 9), (2, 4, 5, 10, 7), (2, 4, 5, 10, 3), (2, 4, 5, 10, 6), (2, 4, 5, 10, 1), (2, 4, 5, 9, 7), (2, 4, 5, 9, 3), (2, 4, 5, 9, 6), (2, 4, 5, 9, 1), (2, 4, 5, 7, 3), (2, 4, 5, 7, 6), (2, 4, 5, 7, 1), (2, 4, 5, 3, 6), (2, 4, 5, 3, 1), (2, 4, 5, 6, 1), (2, 4, 10, 9, 7), (2, 4, 10, 9, 3), (2, 4, 10, 9, 6), (2, 4, 10, 9, 1), (2, 4, 10, 7, 3), (2, 4, 10, 7, 6), (2, 4, 10, 7, 1), (2, 4, 10, 3, 6), (2, 4, 10, 3, 1), (2, 4, 10, 6, 1), (2, 4, 9, 7, 3), (2, 4, 9, 7, 6), (2, 4, 9, 7, 1), (2, 4, 9, 3, 6), (2, 4, 9, 3, 1), (2, 4, 9, 6, 1), (2, 4, 7, 3, 6), (2, 4, 7, 3, 1), (2, 4, 7, 6, 1), (2, 4, 3, 6, 1), (2, 8, 5, 10, 9), (2, 8, 5, 10, 7), (2, 8, 5, 10, 3), (2, 8, 5, 10, 6), (2, 8, 5, 10, 1), (2, 8, 5, 9, 7), (2, 8, 5, 9, 3), (2, 8, 5, 9, 6), (2, 8, 5, 9, 1), (2, 8, 5, 7, 3), (2, 8, 5, 7, 6), (2, 8, 5, 7, 1), (2, 8, 5, 3, 6), (2, 8, 5, 3, 1), (2, 8, 5, 6, 1), (2, 8, 10, 9, 7), (2, 8, 10, 9, 3), (2, 8, 10, 9, 6), (2, 8, 10, 9, 1), (2, 8, 10, 7, 3), (2, 8, 10, 7, 6), (2, 8, 10, 7, 1), (2, 8, 10, 3, 6), (2, 8, 10, 3, 1), (2, 8, 10, 6, 1), (2, 8, 9, 7, 3), (2, 8, 9, 7, 6), (2, 8, 9, 7, 1), (2, 8, 9, 3, 6), (2, 8, 9, 3, 1), (2, 8, 9, 6, 1), (2, 8, 7, 3, 6), (2, 8, 7, 3, 1), (2, 8, 7, 6, 1), (2, 8, 3, 6, 1), (2, 5, 10, 9, 7), (2, 5, 10, 9, 3), (2, 5, 10, 9, 6), (2, 5, 10, 9, 1), (2, 5, 10, 7, 3), (2, 5, 10, 7, 6), (2, 5, 10, 7, 1), (2, 5, 10, 3, 6), (2, 5, 10, 3, 1), (2, 5, 10, 6, 1), (2, 5, 9, 7, 3), (2, 5, 9, 7, 6), (2, 5, 9, 7, 1), (2, 5, 9, 3, 6), (2, 5, 9, 3, 1), (2, 5, 9, 6, 1), (2, 5, 7, 3, 6), (2, 5, 7, 3, 1), (2, 5, 7, 6, 1), (2, 5, 3, 6, 1), (2, 10, 9, 7, 3), (2, 10, 9, 7, 6), (2, 10, 9, 7, 1), (2, 10, 9, 3, 6), (2, 10, 9, 3, 1), (2, 10, 9, 6, 1), (2, 10, 7, 3, 6), (2, 10, 7, 3, 1), (2, 10, 7, 6, 1), (2, 10, 3, 6, 1), (2, 9, 7, 3, 6), (2, 9, 7, 3, 1), (2, 9, 7, 6, 1), (2, 9, 3, 6, 1), (2, 7, 3, 6, 1), 
(4, 8, 5, 10, 9), (4, 8, 5, 10, 7), (4, 8, 5, 10, 3), (4, 8, 5, 10, 6), (4, 8, 5, 10, 1), (4, 8, 5, 9, 7), (4, 8, 5, 9, 3), (4, 8, 5, 9, 6), (4, 8, 5, 9, 1), (4, 8, 5, 7, 3), (4, 8, 5, 7, 6), (4, 8, 5, 7, 1), (4, 8, 5, 3, 6), (4, 8, 5, 3, 1), (4, 8, 5, 6, 1), (4, 8, 10, 9, 7), (4, 8, 10, 9, 3), (4, 8, 10, 9, 6), (4, 8, 10, 9, 1), (4, 8, 10, 7, 3), (4, 8, 10, 7, 6), (4, 8, 10, 7, 1), (4, 8, 10, 3, 6), (4, 8, 10, 3, 1), (4, 8, 10, 6, 1), (4, 8, 9, 7, 3), (4, 8, 9, 7, 6), (4, 8, 9, 7, 1), (4, 8, 9, 3, 6), (4, 8, 9, 3, 1), (4, 8, 9, 6, 1), (4, 8, 7, 3, 6), (4, 8, 7, 3, 1), (4, 8, 7, 6, 1), (4, 8, 3, 6, 1), (4, 5, 10, 9, 7), (4, 5, 10, 9, 3), (4, 5, 10, 9, 6), (4, 5, 10, 9, 1), (4, 5, 10, 7, 3), (4, 5, 10, 7, 6), (4, 5, 10, 7, 1), (4, 5, 10, 3, 6), (4, 5, 10, 3, 1), (4, 5, 10, 6, 1), (4, 5, 9, 7, 3), (4, 5, 9, 7, 6), (4, 5, 9, 7, 1), (4, 5, 9, 3, 6), (4, 5, 9, 3, 1), (4, 5, 9, 6, 1), (4, 5, 7, 3, 6), (4, 5, 7, 3, 1), (4, 5, 7, 6, 1), (4, 5, 3, 6, 1), (4, 10, 9, 7, 3), (4, 10, 9, 7, 6), (4, 10, 9, 7, 1), (4, 10, 9, 3, 6), (4, 10, 9, 3, 1), (4, 10, 9, 6, 1), (4, 10, 7, 3, 6), (4, 10, 7, 3, 1), (4, 10, 7, 6, 1), (4, 10, 3, 6, 1), (4, 9, 7, 3, 6), (4, 9, 7, 3, 1), (4, 9, 7, 6, 1), (4, 9, 3, 6, 1), (4, 7, 3, 6, 1), 
(8, 5, 10, 9, 7), (8, 5, 10, 9, 3), (8, 5, 10, 9, 6), (8, 5, 10, 9, 1), (8, 5, 10, 7, 3), (8, 5, 10, 7, 6), (8, 5, 10, 7, 1), (8, 5, 10, 3, 6), (8, 5, 10, 3, 1), (8, 5, 10, 6, 1), (8, 5, 9, 7, 3), (8, 5, 9, 7, 6), (8, 5, 9, 7, 1), (8, 5, 9, 3, 6), (8, 5, 9, 3, 1), (8, 5, 9, 6, 1), (8, 5, 7, 3, 6), (8, 5, 7, 3, 1), (8, 5, 7, 6, 1), (8, 5, 3, 6, 1), (8, 10, 9, 7, 3), (8, 10, 9, 7, 6), (8, 10, 9, 7, 1), (8, 10, 9, 3, 6), (8, 10, 9, 3, 1), (8, 10, 9, 6, 1), (8, 10, 7, 3, 6), (8, 10, 7, 3, 1), (8, 10, 7, 6, 1), (8, 10, 3, 6, 1), (8, 9, 7, 3, 6), (8, 9, 7, 3, 1), (8, 9, 7, 6, 1), (8, 9, 3, 6, 1), (8, 7, 3, 6, 1), 
(5, 10, 9, 7, 3), (5, 10, 9, 7, 6), (5, 10, 9, 7, 1), (5, 10, 9, 3, 6), (5, 10, 9, 3, 1), (5, 10, 9, 6, 1), (5, 10, 7, 3, 6), (5, 10, 7, 3, 1), (5, 10, 7, 6, 1), (5, 10, 3, 6, 1), (5, 9, 7, 3, 6), (5, 9, 7, 3, 1), (5, 9, 7, 6, 1), (5, 9, 3, 6, 1), (5, 7, 3, 6, 1), 
(10, 9, 7, 3, 6), (10, 9, 7, 3, 1), (10, 9, 7, 6, 1), (10, 9, 3, 6, 1), (10, 7, 3, 6, 1), 
(9, 7, 3, 6, 1), 
(2, 4, 8, 5, 10, 9), (2, 4, 8, 5, 10, 7), (2, 4, 8, 5, 10, 3), (2, 4, 8, 5, 10, 6), (2, 4, 8, 5, 10, 1), (2, 4, 8, 5, 9, 7), (2, 4, 8, 5, 9, 3), (2, 4, 8, 5, 9, 6), (2, 4, 8, 5, 9, 1), (2, 4, 8, 5, 7, 3), (2, 4, 8, 5, 7, 6), (2, 4, 8, 5, 7, 1), (2, 4, 8, 5, 3, 6), (2, 4, 8, 5, 3, 1), (2, 4, 8, 5, 6, 1), (2, 4, 8, 10, 9, 7), (2, 4, 8, 10, 9, 3), (2, 4, 8, 10, 9, 6), (2, 4, 8, 10, 9, 1), (2, 4, 8, 10, 7, 3), (2, 4, 8, 10, 7, 6), (2, 4, 8, 10, 7, 1), (2, 4, 8, 10, 3, 6), (2, 4, 8, 10, 3, 1), (2, 4, 8, 10, 6, 1), (2, 4, 8, 9, 7, 3), (2, 4, 8, 9, 7, 6), (2, 4, 8, 9, 7, 1), (2, 4, 8, 9, 3, 6), (2, 4, 8, 9, 3, 1), (2, 4, 8, 9, 6, 1), (2, 4, 8, 7, 3, 6), (2, 4, 8, 7, 3, 1), (2, 4, 8, 7, 6, 1), (2, 4, 8, 3, 6, 1), (2, 4, 5, 10, 9, 7), (2, 4, 5, 10, 9, 3), (2, 4, 5, 10, 9, 6), (2, 4, 5, 10, 9, 1), (2, 4, 5, 10, 7, 3), (2, 4, 5, 10, 7, 6), (2, 4, 5, 10, 7, 1), (2, 4, 5, 10, 3, 6), (2, 4, 5, 10, 3, 1), (2, 4, 5, 10, 6, 1), (2, 4, 5, 9, 7, 3), (2, 4, 5, 9, 7, 6), (2, 4, 5, 9, 7, 1), (2, 4, 5, 9, 3, 6), (2, 4, 5, 9, 3, 1), (2, 4, 5, 9, 6, 1), (2, 4, 5, 7, 3, 6), (2, 4, 5, 7, 3, 1), (2, 4, 5, 7, 6, 1), (2, 4, 5, 3, 6, 1), (2, 4, 10, 9, 7, 3), (2, 4, 10, 9, 7, 6), (2, 4, 10, 9, 7, 1), (2, 4, 10, 9, 3, 6), (2, 4, 10, 9, 3, 1), (2, 4, 10, 9, 6, 1), (2, 4, 10, 7, 3, 6), (2, 4, 10, 7, 3, 1), (2, 4, 10, 7, 6, 1), (2, 4, 10, 3, 6, 1), (2, 4, 9, 7, 3, 6), (2, 4, 9, 7, 3, 1), (2, 4, 9, 7, 6, 1), (2, 4, 9, 3, 6, 1), (2, 4, 7, 3, 6, 1), (2, 8, 5, 10, 9, 7), (2, 8, 5, 10, 9, 3), (2, 8, 5, 10, 9, 6), (2, 8, 5, 10, 9, 1), (2, 8, 5, 10, 7, 3), (2, 8, 5, 10, 7, 6), (2, 8, 5, 10, 7, 1), (2, 8, 5, 10, 3, 6), (2, 8, 5, 10, 3, 1), (2, 8, 5, 10, 6, 1), (2, 8, 5, 9, 7, 3), (2, 8, 5, 9, 7, 6), (2, 8, 5, 9, 7, 1), (2, 8, 5, 9, 3, 6), (2, 8, 5, 9, 3, 1), (2, 8, 5, 9, 6, 1), (2, 8, 5, 7, 3, 6), (2, 8, 5, 7, 3, 1), (2, 8, 5, 7, 6, 1), (2, 8, 5, 3, 6, 1), (2, 8, 10, 9, 7, 3), (2, 8, 10, 9, 7, 6), (2, 8, 10, 9, 7, 1), (2, 8, 10, 9, 3, 6), (2, 8, 10, 9, 3, 1), (2, 8, 10, 9, 6, 1), (2, 8, 10, 7, 3, 6), (2, 8, 10, 7, 3, 1), (2, 8, 10, 7, 6, 1), (2, 8, 10, 3, 6, 1), (2, 8, 9, 7, 3, 6), (2, 8, 9, 7, 3, 1), (2, 8, 9, 7, 6, 1), (2, 8, 9, 3, 6, 1), (2, 8, 7, 3, 6, 1), (2, 5, 10, 9, 7, 3), (2, 5, 10, 9, 7, 6), (2, 5, 10, 9, 7, 1), (2, 5, 10, 9, 3, 6), (2, 5, 10, 9, 3, 1), (2, 5, 10, 9, 6, 1), (2, 5, 10, 7, 3, 6), (2, 5, 10, 7, 3, 1), (2, 5, 10, 7, 6, 1), (2, 5, 10, 3, 6, 1), (2, 5, 9, 7, 3, 6), (2, 5, 9, 7, 3, 1), (2, 5, 9, 7, 6, 1), (2, 5, 9, 3, 6, 1), (2, 5, 7, 3, 6, 1), (2, 10, 9, 7, 3, 6), (2, 10, 9, 7, 3, 1), (2, 10, 9, 7, 6, 1), (2, 10, 9, 3, 6, 1), (2, 10, 7, 3, 6, 1), (2, 9, 7, 3, 6, 1), 
(4, 8, 5, 10, 9, 7), (4, 8, 5, 10, 9, 3), (4, 8, 5, 10, 9, 6), (4, 8, 5, 10, 9, 1), (4, 8, 5, 10, 7, 3), (4, 8, 5, 10, 7, 6), (4, 8, 5, 10, 7, 1), (4, 8, 5, 10, 3, 6), (4, 8, 5, 10, 3, 1), (4, 8, 5, 10, 6, 1), (4, 8, 5, 9, 7, 3), (4, 8, 5, 9, 7, 6), (4, 8, 5, 9, 7, 1), (4, 8, 5, 9, 3, 6), (4, 8, 5, 9, 3, 1), (4, 8, 5, 9, 6, 1), (4, 8, 5, 7, 3, 6), (4, 8, 5, 7, 3, 1), (4, 8, 5, 7, 6, 1), (4, 8, 5, 3, 6, 1), (4, 8, 10, 9, 7, 3), (4, 8, 10, 9, 7, 6), (4, 8, 10, 9, 7, 1), (4, 8, 10, 9, 3, 6), (4, 8, 10, 9, 3, 1), (4, 8, 10, 9, 6, 1), (4, 8, 10, 7, 3, 6), (4, 8, 10, 7, 3, 1), (4, 8, 10, 7, 6, 1), (4, 8, 10, 3, 6, 1), (4, 8, 9, 7, 3, 6), (4, 8, 9, 7, 3, 1), (4, 8, 9, 7, 6, 1), (4, 8, 9, 3, 6, 1), (4, 8, 7, 3, 6, 1), (4, 5, 10, 9, 7, 3), (4, 5, 10, 9, 7, 6), (4, 5, 10, 9, 7, 1), (4, 5, 10, 9, 3, 6), (4, 5, 10, 9, 3, 1), (4, 5, 10, 9, 6, 1), (4, 5, 10, 7, 3, 6), (4, 5, 10, 7, 3, 1), (4, 5, 10, 7, 6, 1), (4, 5, 10, 3, 6, 1), (4, 5, 9, 7, 3, 6), (4, 5, 9, 7, 3, 1), (4, 5, 9, 7, 6, 1), (4, 5, 9, 3, 6, 1), (4, 5, 7, 3, 6, 1), (4, 10, 9, 7, 3, 6), (4, 10, 9, 7, 3, 1), (4, 10, 9, 7, 6, 1), (4, 10, 9, 3, 6, 1), (4, 10, 7, 3, 6, 1), (4, 9, 7, 3, 6, 1), 
(8, 5, 10, 9, 7, 3), (8, 5, 10, 9, 7, 6), (8, 5, 10, 9, 7, 1), (8, 5, 10, 9, 3, 6), (8, 5, 10, 9, 3, 1), (8, 5, 10, 9, 6, 1), (8, 5, 10, 7, 3, 6), (8, 5, 10, 7, 3, 1), (8, 5, 10, 7, 6, 1), (8, 5, 10, 3, 6, 1), (8, 5, 9, 7, 3, 6), (8, 5, 9, 7, 3, 1), (8, 5, 9, 7, 6, 1), (8, 5, 9, 3, 6, 1), (8, 5, 7, 3, 6, 1), (8, 10, 9, 7, 3, 6), (8, 10, 9, 7, 3, 1), (8, 10, 9, 7, 6, 1), (8, 10, 9, 3, 6, 1), (8, 10, 7, 3, 6, 1), (8, 9, 7, 3, 6, 1), 
(5, 10, 9, 7, 3, 6), (5, 10, 9, 7, 3, 1), (5, 10, 9, 7, 6, 1), (5, 10, 9, 3, 6, 1), (5, 10, 7, 3, 6, 1), (5, 9, 7, 3, 6, 1), 
(10, 9, 7, 3, 6, 1), 
(2, 4, 8, 5, 10, 9, 7), (2, 4, 8, 5, 10, 9, 3), (2, 4, 8, 5, 10, 9, 6), (2, 4, 8, 5, 10, 9, 1), (2, 4, 8, 5, 10, 7, 3), (2, 4, 8, 5, 10, 7, 6), (2, 4, 8, 5, 10, 7, 1), (2, 4, 8, 5, 10, 3, 6), (2, 4, 8, 5, 10, 3, 1), (2, 4, 8, 5, 10, 6, 1), (2, 4, 8, 5, 9, 7, 3), (2, 4, 8, 5, 9, 7, 6), (2, 4, 8, 5, 9, 7, 1), (2, 4, 8, 5, 9, 3, 6), (2, 4, 8, 5, 9, 3, 1), (2, 4, 8, 5, 9, 6, 1), (2, 4, 8, 5, 7, 3, 6), (2, 4, 8, 5, 7, 3, 1), (2, 4, 8, 5, 7, 6, 1), (2, 4, 8, 5, 3, 6, 1), (2, 4, 8, 10, 9, 7, 3), (2, 4, 8, 10, 9, 7, 6), (2, 4, 8, 10, 9, 7, 1), (2, 4, 8, 10, 9, 3, 6), (2, 4, 8, 10, 9, 3, 1), (2, 4, 8, 10, 9, 6, 1), (2, 4, 8, 10, 7, 3, 6), (2, 4, 8, 10, 7, 3, 1), (2, 4, 8, 10, 7, 6, 1), (2, 4, 8, 10, 3, 6, 1), (2, 4, 8, 9, 7, 3, 6), (2, 4, 8, 9, 7, 3, 1), (2, 4, 8, 9, 7, 6, 1), (2, 4, 8, 9, 3, 6, 1), (2, 4, 8, 7, 3, 6, 1), (2, 4, 5, 10, 9, 7, 3), (2, 4, 5, 10, 9, 7, 6), (2, 4, 5, 10, 9, 7, 1), (2, 4, 5, 10, 9, 3, 6), (2, 4, 5, 10, 9, 3, 1), (2, 4, 5, 10, 9, 6, 1), (2, 4, 5, 10, 7, 3, 6), (2, 4, 5, 10, 7, 3, 1), (2, 4, 5, 10, 7, 6, 1), (2, 4, 5, 10, 3, 6, 1), (2, 4, 5, 9, 7, 3, 6), (2, 4, 5, 9, 7, 3, 1), (2, 4, 5, 9, 7, 6, 1), (2, 4, 5, 9, 3, 6, 1), (2, 4, 5, 7, 3, 6, 1), (2, 4, 10, 9, 7, 3, 6), (2, 4, 10, 9, 7, 3, 1), (2, 4, 10, 9, 7, 6, 1), (2, 4, 10, 9, 3, 6, 1), (2, 4, 10, 7, 3, 6, 1), (2, 4, 9, 7, 3, 6, 1), (2, 8, 5, 10, 9, 7, 3), (2, 8, 5, 10, 9, 7, 6), (2, 8, 5, 10, 9, 7, 1), (2, 8, 5, 10, 9, 3, 6), (2, 8, 5, 10, 9, 3, 1), (2, 8, 5, 10, 9, 6, 1), (2, 8, 5, 10, 7, 3, 6), (2, 8, 5, 10, 7, 3, 1), (2, 8, 5, 10, 7, 6, 1), (2, 8, 5, 10, 3, 6, 1), (2, 8, 5, 9, 7, 3, 6), (2, 8, 5, 9, 7, 3, 1), (2, 8, 5, 9, 7, 6, 1), (2, 8, 5, 9, 3, 6, 1), (2, 8, 5, 7, 3, 6, 1), (2, 8, 10, 9, 7, 3, 6), (2, 8, 10, 9, 7, 3, 1), (2, 8, 10, 9, 7, 6, 1), (2, 8, 10, 9, 3, 6, 1), (2, 8, 10, 7, 3, 6, 1), (2, 8, 9, 7, 3, 6, 1), (2, 5, 10, 9, 7, 3, 6), (2, 5, 10, 9, 7, 3, 1), (2, 5, 10, 9, 7, 6, 1), (2, 5, 10, 9, 3, 6, 1), (2, 5, 10, 7, 3, 6, 1), (2, 5, 9, 7, 3, 6, 1), (2, 10, 9, 7, 3, 6, 1), 
(4, 8, 5, 10, 9, 7, 3), (4, 8, 5, 10, 9, 7, 6), (4, 8, 5, 10, 9, 7, 1), (4, 8, 5, 10, 9, 3, 6), (4, 8, 5, 10, 9, 3, 1), (4, 8, 5, 10, 9, 6, 1), (4, 8, 5, 10, 7, 3, 6), (4, 8, 5, 10, 7, 3, 1), (4, 8, 5, 10, 7, 6, 1), (4, 8, 5, 10, 3, 6, 1), (4, 8, 5, 9, 7, 3, 6), (4, 8, 5, 9, 7, 3, 1), (4, 8, 5, 9, 7, 6, 1), (4, 8, 5, 9, 3, 6, 1), (4, 8, 5, 7, 3, 6, 1), (4, 8, 10, 9, 7, 3, 6), (4, 8, 10, 9, 7, 3, 1), (4, 8, 10, 9, 7, 6, 1), (4, 8, 10, 9, 3, 6, 1), (4, 8, 10, 7, 3, 6, 1), (4, 8, 9, 7, 3, 6, 1), (4, 5, 10, 9, 7, 3, 6), (4, 5, 10, 9, 7, 3, 1), (4, 5, 10, 9, 7, 6, 1), (4, 5, 10, 9, 3, 6, 1), (4, 5, 10, 7, 3, 6, 1), (4, 5, 9, 7, 3, 6, 1), (4, 10, 9, 7, 3, 6, 1), 
(8, 5, 10, 9, 7, 3, 6), (8, 5, 10, 9, 7, 3, 1), (8, 5, 10, 9, 7, 6, 1), (8, 5, 10, 9, 3, 6, 1), (8, 5, 10, 7, 3, 6, 1), (8, 5, 9, 7, 3, 6, 1), (8, 10, 9, 7, 3, 6, 1), 
(5, 10, 9, 7, 3, 6, 1), 
(2, 4, 8, 5, 10, 9, 7, 3), (2, 4, 8, 5, 10, 9, 7, 6), (2, 4, 8, 5, 10, 9, 7, 1), (2, 4, 8, 5, 10, 9, 3, 6), (2, 4, 8, 5, 10, 9, 3, 1), (2, 4, 8, 5, 10, 9, 6, 1), (2, 4, 8, 5, 10, 7, 3, 6), (2, 4, 8, 5, 10, 7, 3, 1), (2, 4, 8, 5, 10, 7, 6, 1), (2, 4, 8, 5, 10, 3, 6, 1), (2, 4, 8, 5, 9, 7, 3, 6), (2, 4, 8, 5, 9, 7, 3, 1), (2, 4, 8, 5, 9, 7, 6, 1), (2, 4, 8, 5, 9, 3, 6, 1), (2, 4, 8, 5, 7, 3, 6, 1), (2, 4, 8, 10, 9, 7, 3, 6), (2, 4, 8, 10, 9, 7, 3, 1), (2, 4, 8, 10, 9, 7, 6, 1), (2, 4, 8, 10, 9, 3, 6, 1), (2, 4, 8, 10, 7, 3, 6, 1), (2, 4, 8, 9, 7, 3, 6, 1), (2, 4, 5, 10, 9, 7, 3, 6), (2, 4, 5, 10, 9, 7, 3, 1), (2, 4, 5, 10, 9, 7, 6, 1), (2, 4, 5, 10, 9, 3, 6, 1), (2, 4, 5, 10, 7, 3, 6, 1), (2, 4, 5, 9, 7, 3, 6, 1), (2, 4, 10, 9, 7, 3, 6, 1), (2, 8, 5, 10, 9, 7, 3, 6), (2, 8, 5, 10, 9, 7, 3, 1), (2, 8, 5, 10, 9, 7, 6, 1), (2, 8, 5, 10, 9, 3, 6, 1), (2, 8, 5, 10, 7, 3, 6, 1), (2, 8, 5, 9, 7, 3, 6, 1), (2, 8, 10, 9, 7, 3, 6, 1), (2, 5, 10, 9, 7, 3, 6, 1), 
(4, 8, 5, 10, 9, 7, 3, 6), (4, 8, 5, 10, 9, 7, 3, 1), (4, 8, 5, 10, 9, 7, 6, 1), (4, 8, 5, 10, 9, 3, 6, 1), (4, 8, 5, 10, 7, 3, 6, 1), (4, 8, 5, 9, 7, 3, 6, 1), (4, 8, 10, 9, 7, 3, 6, 1), (4, 5, 10, 9, 7, 3, 6, 1), 
(8, 5, 10, 9, 7, 3, 6, 1), 
(2, 4, 8, 5, 10, 9, 7, 3, 6), (2, 4, 8, 5, 10, 9, 7, 3, 1), (2, 4, 8, 5, 10, 9, 7, 6, 1), (2, 4, 8, 5, 10, 9, 3, 6, 1), (2, 4, 8, 5, 10, 7, 3, 6, 1), (2, 4, 8, 5, 9, 7, 3, 6, 1), (2, 4, 8, 10, 9, 7, 3, 6, 1), (2, 4, 5, 10, 9, 7, 3, 6, 1), (2, 8, 5, 10, 9, 7, 3, 6, 1), 
(4, 8, 5, 10, 9, 7, 3, 6, 1), 
(2, 4, 8, 5, 10, 9, 7, 3, 6, 1)], 

[(8, 10, 6), 
(2, 9, 7, 3, 6), (2, 4, 8, 5, 10, 7, 3), (2, 8, 10, 3, 6), 
(4, 3), 
(2, 4, 8, 5, 7, 1), 
(5, 9, 6, 1), 
(8, 7, 3, 6, 1), 
(2, 8, 5, 3, 6, 1), 
(8, 5, 6, 1), 
(2, 4, 5, 10, 7, 3, 6), (2, 4, 8, 9, 6, 1), (2, 5, 10, 3, 6), (2, 4, 5, 9, 7, 1), (2, 5, 9, 6, 1), 
(4, 9, 7, 1), 
(8, 5, 10, 9, 7), 
(2, 4, 8, 10, 9, 6, 1), (2, 4, 8, 5, 7, 6), 
(8, 9, 3, 6), 
(5, 10, 6, 1), 
(8, 10, 7, 6, 1), 
(2, 10, 3), 
(5, 9, 7, 6, 1), 
(2, 8, 5, 10, 9, 3, 6, 1), (2, 9, 7, 6, 1), 
(10, 3), 
(5, 9, 7, 3, 6), 
(10, 9, 7, 1), 
(2, 9, 7, 3, 6, 1), 
(5, 9, 1), 
(2, 4, 8, 10, 7, 3, 1), 
(4, 8, 5, 10, 1), (4, 8, 5, 10, 7, 6), 
(8, 10, 1), 
(2, 8, 9, 1), 
(4, 8, 10, 6), (4, 8, 5, 10, 9, 3, 1), (4, 8, 5, 10, 6), 
(2, 4, 8, 9, 3, 6), 
(4, 8, 9, 7, 3), 
(2, 5, 9, 7, 1), 
(4, 7, 3, 1), 
(2, 4, 5, 3), (2, 4, 8, 5, 9, 7, 1), (2, 4, 10, 7, 3), (2, 4, 8, 10, 7, 3, 6, 1), 
(7, 6, 1), 
(2, 8, 5, 10, 3), (2, 4, 8, 5, 10, 9, 7, 1), 
(8, 10, 9, 7, 3, 6, 1), 
(4, 8, 5, 10, 9, 7, 3, 6, 1), 
(2, 5, 9, 7, 3, 1), 
(4, 8, 7, 3, 6), 
(8, 5, 10, 3), 
(2, 4, 5, 10, 3), 
(4, 8, 10, 7, 6), 
(2, 5, 10, 7, 3, 6, 1), 
(5, 6, 1), 
(10, 7, 3), 
(2, 8, 9, 7), (2, 4, 10, 9, 7, 3, 6), (2, 4, 8, 9, 7, 1), 
(5, 10, 9, 3), 
(10, 7, 3, 6), 
(2, 4, 8, 10, 3, 6), 
(9, 7, 1), 
(4, 5, 10, 9, 3, 1), 
(7, 6), 
(2, 4, 8, 5, 10, 9, 6, 1), 
(4, 10, 3, 1), (4, 8, 9, 3, 6), 
(8, 5, 10, 3, 6, 1), 
(2, 4, 8, 10, 7, 6, 1), (2, 4, 9, 7), (2, 8, 5, 10, 9, 7, 6), 
(4, 8, 5, 9, 3, 1), 
(5, 10, 9, 7, 3, 6, 1), 
(4, 5, 10, 9, 7, 1), 
(2, 4, 5, 1), 
(4, 8, 10, 9, 7, 3, 1), (4, 9, 3, 1), (4, 7, 6, 1), 
(2, 8, 5, 9, 6), 
(8, 7, 3), 
(4, 5, 10, 7, 3, 6), 
(2, 4, 5, 7, 6, 1), (2, 8, 10, 6), 
(10, 9, 7), 
(4, 8, 5, 10, 9, 7), 
(2, 10, 9), (2, 4, 10, 3), 
(4, 8, 5, 9), 
(2, 3), 
(8, 5, 10, 9, 6, 1), (8, 9, 6, 1), 
(5, 10, 3, 1), 
(8, 9, 3, 1), 
(5, 10, 7, 6, 1), 
(2, 5, 10, 1), (2, 8, 5, 10, 6), 
(5, 3, 1), 
(4, 8, 7, 3, 6, 1), 
(5, 3, 6), 
(2, 4, 5, 7, 3), 
(4, 8, 10, 9, 3, 1), 
(2, 4, 5, 10, 9, 7, 3, 1), 
(4, 5, 7, 3, 6, 1), 
(2, 8, 10, 9, 7, 3, 1), (2, 4, 8, 5, 9, 1), (2, 4, 8, 10, 7), (2, 4, 8, 10, 9, 6), (2, 4, 8, 5, 10, 9, 7, 3, 1), 
(4, 8, 5, 9, 7, 3, 1), 
(2, 4, 8, 5, 10, 6, 1), (2, 4, 10, 9, 7), 
(4, 8, 10, 7), (2, 4, 8, 5, 9, 7, 6), 
(10, 9), 
(2, 5, 9, 3), 
(4, 5, 9, 1), 
(2, 8, 10, 9, 1), 
(4, 5, 7, 3, 1), 
(2, 8, 5, 10, 9, 3), (2, 8, 10, 3, 6, 1), (2, 4, 8, 7, 6, 1), (2, 8, 10, 7, 1), (2, 4, 5, 9), 
(10, 3, 6), 
(2, 4, 7, 6, 1), 
(8, 5, 10, 9, 3, 6), (8, 5, 10, 9, 3, 1), 
(4, 8, 10, 3, 6, 1), 
(2, 8, 5, 10, 9, 7, 3, 6, 1), 
(8, 5, 9, 7, 3, 6, 1), 
(2, 4, 8, 5, 9, 7, 3, 6), (2, 8, 5, 9, 3, 6, 1), (2, 4, 8, 5, 10, 7), (2, 10, 9, 1), 
(9, 3, 6), 
(2, 5, 7, 3, 1), 
(5, 10, 9, 3, 6), (5, 7, 1), 
(2, 5, 7, 3, 6, 1), 
(4, 10, 9, 7), 
(2, 5, 10, 9, 7, 3, 6, 1), (2, 5, 9, 7), (4, 8, 5, 7, 3), (2, 4, 10, 9, 7, 3, 1), (2, 8, 5, 9, 1), 
(8, 10, 7, 3, 1), 
(2, 4, 8, 10, 7, 3), (2, 10, 9, 7, 1), (2, 4, 8, 9, 3, 6, 1), (2, 9, 1), 
(4, 8, 5, 9, 7, 1), 
(2, 4, 8, 9, 7, 3, 6, 1), 
(4, 5, 10, 9, 7, 3, 1), 
(2, 4, 5, 9, 3), 
(10, 9, 3, 6, 1), 
(4, 10, 7, 1), 
(8, 6), 
(9, 7, 6), 
(5, 7, 3), 
(2, 4, 8, 5, 10, 9, 1), 
(10, 7), 
(2, 4, 7, 3, 1), 
(8, 5, 9, 3, 6), 
(4, 8, 5, 9, 7, 6, 1), (4, 8, 5, 10, 7, 3, 1), 
(2, 4, 5, 10, 9, 7, 3, 6), (2, 4, 9, 7, 3, 6), 
(10, 6, 1), 
(2, 8, 5, 10, 9, 7, 6, 1), 
(8, 3), 
(2, 6), 
(3, 6), 
(9, 3, 1), 
(8, 5, 10, 9, 7, 3, 6), 
(2, 4, 8, 5, 3, 1), (2, 9, 7, 3, 1), (2, 10, 7, 3, 6, 1), 
(8, 5, 10, 3, 6), 
(10, 9, 7, 3, 6, 1), 
(2, 5, 10, 9), (2, 3, 6), 
(4, 8, 10, 9, 7, 3, 6, 1), (4, 8, 5, 9, 6), 
(2, 4, 5, 9, 7, 3, 1), 
(4, 8, 10, 7, 3, 1), 
(8, 5, 10, 7, 3), (8, 5, 10, 7, 6), 
(4, 8, 9, 7, 6), 
(2, 10, 9, 6), (2, 5, 10, 9, 6, 1), 
(4, 5, 3, 6), 
(2, 4, 8, 10, 7, 3, 6), 
(5, 9, 3), 
(4, 8, 9, 3, 6, 1), 
(2, 4, 8, 5, 10, 9, 7), (2, 8, 3), 
(4, 5, 10, 6), 
(2, 8, 7, 3, 6, 1), 
(8, 6, 1), 
(4, 8, 10, 9), 
(2, 4, 9, 3, 6, 1), (2, 4, 5, 10, 9, 7, 1), 
(10, 7, 3, 1), 
(8, 5, 10, 9, 7, 3, 6, 1), 
(2, 4, 8, 10, 6, 1), 
(10, 9, 3, 1), 
(2, 4, 5, 9, 3, 1)], 
(), 
(),
 1024) 1024 elementos que es 2^10, 10 son las "partes"
'''

print("\n")

print("LSSS: is linear: ")
print(LSSS.LSSS.lsss(ciclo1,11))

'''
True
'''

print("\n")

print("Funcion phi: ")
print(CP_ABE.CP_ABE.phiFunction(16))

'''
Funcion phi:
8
'''

print("\n")

print("Setup: ")
print(CP_ABE.CP_ABE.setup(CP_ABE.CP_ABE.phiFunction(16), 3, 11))

'''
([[2, 4, 8, 5, 10, 9, 7, 3, 6, 1], 2, [16384, 268435456, 0, 1808548329, 276447232, 1796636465, -381759919, 4782969, 1054752768, 1], 8, [4, 5, 9]], 
128)
'''

print("\n")

pk, msk, gElevaleA, h = CP_ABE.CP_ABE.setup(CP_ABE.CP_ABE.phiFunction(16), 3, 11) 

print("KeyGen: ")
print(CP_ABE.CP_ABE.keyGen(msk, h, 11, gElevaleA))

'''
[4096, 2, [3, 4, 8]]
'''

print("\n")

print(CP_ABE.CP_ABE.encrypt(pk,"hello world",structureA)) # sustituir si es necesario