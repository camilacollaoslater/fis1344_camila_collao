import numpy as np

def secante(f, p0, p1, epsilon=1e-10, N=100):
    for _ in range(N):
        q0, q1 = f(p0), f(p1)
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) / abs(p) < epsilon:
            return p
        p0, p1 = p1, p
    raise ValueError("La secante no convergio.")


#conté los años desde 1960 y usé las poblaciones tal como están en la tabla.
P0, P1, P2 = 179323, 203302, 226542

#usé las diferencias de 1/P entre décadas para obtener una ecuación que dependa solo de k.
def f(k):
    return (1 / P0 - 1 / P1) * np.exp(-10 * k) - (1 / P1 - 1 / P2)

k = secante(f, 0.01, 0.02)
#con el valor de k, calculé PL y c usando los datos de 1960 y 1970.
q = np.exp(-10 * k)
PL = (1 - q) / (1 / P1 - q / P0)
c = 1 - PL / P0

def poblacion(anio):
    return PL / (1 - c * np.exp(-k * (anio - 1960)))

P1990 = poblacion(1990)
P2020 = poblacion(2020)
real_1990 = 249633
error_relativo = abs(P1990 - real_1990) / real_1990 * 100

print(f"c = {c:.8f}")
print(f"k = {k:.8f} por año")
print(f"P_L = {PL:.3f}")
print(f"Prediccion para 1990:{P1990:.3f}")
print(f"Prediccion para 2020:{P2020:.3f}")
print(f"Poblacion real en 1990:{real_1990}")
print(f"El modelo subestima la poblacion de 1990 en {error_relativo:.4f}%.")

# Nota: 7.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 1/1; claridad: 1/1.
