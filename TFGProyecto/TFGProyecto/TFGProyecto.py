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



print("\n")

print("LSSS: is linear: ")
print(LSSS.LSSS.lsss(ciclo1))

print("\n")

print("Funcion phi: ")
print(CP_ABE.CP_ABE.phiFunction(16))

'''
Funcion phi:
8
'''

print("\n")

print("Setup: ")
print(CP_ABE.CP_ABE.setup(None, 5, 7)) # cambiar mas tarde