import BilinearMaps

ciclo1= BilinearMaps.BilinearMaps.cyclic(11)
ciclo2 = BilinearMaps.BilinearMaps.cyclic(13)

print("Ciclo 1: ")
print(ciclo1)

print("\n")

print("G x G -> Gt1: ")
print(BilinearMaps.BilinearMaps.e(ciclo1, ciclo1))

print("\n")

print("G x G -> Gt2: ")
print(BilinearMaps.BilinearMaps.e(ciclo2, ciclo2))

print("\n")

print("Propiedad bilineal: ")
print(BilinearMaps.BilinearMaps.bilinear())