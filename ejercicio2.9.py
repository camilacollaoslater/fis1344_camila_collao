import numpy as np
from math import factorial

def f_obvio(x):
    return (np.exp(x) - 1.0) / x

#serie de Taylor con los primeros ocho terminos
def f_taylor(x):
    resultado = 0.0

    for k in range(8):
        resultado += x**k / factorial(k + 1)

    return resultado

def kappa(x):
    if x == 0:
        return 0.0

    numerador = (x - 1.0) * np.exp(x) + 1.0
    denominador = np.exp(x) - 1.0

    return abs(numerador / denominador)

print("numero de condicionamiento")
print("kappa(-1) =", kappa(-1.0))
print("kappa(0)  =", kappa(0.0))
print("kappa(1)  =", kappa(1.0))
print("Máximo    =", kappa(1.0))

valores_x = 10.0**(-np.arange(2, 9))

print("\ncomparacion de los metodos")

print(
    f"{'x':>10}"
    f"{'metodo obvio':>22}"
    f"{'Taylor':>22}"
    f"{'diferencia relativa':>24}"
)

for x in valores_x:
    obvio = f_obvio(x)
    taylor = f_taylor(x)

    # Diferencia relativa tomando Taylor como referencia
    diferencia_relativa = abs(obvio - taylor) / abs(taylor)

    print(
        f"{x:10.0e}"
        f"{obvio:22.15f}"
        f"{taylor:22.15f}"
        f"{diferencia_relativa:24.3e}"
    )


print("""
Taylor es más preciso. El problema esta bien condicionado (kappa ≈ 0.582),
por lo que el error proviene del algoritmo obvio. Para x pequeño, e^x es
muy cercano a 1 y la resta e^x - 1 produce cancelacion numerica, perdiendo
cifras significativas.

La serie de Taylor evita esta resta y mantiene un error cercano a la
precision de la maquina. Por eso, el algoritmo obvio es inestable cerca
de cero, mientras que Taylor es estable y mas preciso.
""")