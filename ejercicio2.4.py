import numpy as np

print("epsilon de float16:", np.finfo(np.float16).eps)

#suma de 1/n^2 desde n = 1 hasta n = 100
suma_2_directa = np.float16(0.0)

for n in range(1, 101):
    termino = np.float16(1.0 / n**2)
    suma_2_directa = np.float16(suma_2_directa + termino)


#suma de 1/n^2 desde n = 100 hasta n = 1
suma_2_inversa = np.float16(0.0)

for n in range(100, 0, -1):
    termino = np.float16(1.0 / n**2)
    suma_2_inversa = np.float16(suma_2_inversa + termino)

print("suma de 1/n^2")
print("orden directo:", float(suma_2_directa))
print("orden inverso:", float(suma_2_inversa))


#suma de 1/n^3 desde n = 1 hasta n = 100
suma_3_directa = np.float16(0.0)

for n in range(1, 101):
    termino = np.float16(1.0 / n**3)
    suma_3_directa = np.float16(suma_3_directa + termino)


#suma de 1/n^3 desde n = 100 hasta n = 1
suma_3_inversa = np.float16(0.0)

for n in range(100, 0, -1):
    termino = np.float16(1.0 / n**3)
    suma_3_inversa = np.float16(suma_3_inversa + termino)

print("suma de 1/n^3")
print("orden directo:", float(suma_3_directa))
print("orden inverso:", float(suma_3_inversa))
