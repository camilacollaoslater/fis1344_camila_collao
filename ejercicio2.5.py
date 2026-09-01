import numpy as np

def condicionamiento_b(a, b, c):

    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("el polinomio no tiene raices reales.")
        return

    if discriminante == 0:
        raiz = -b / (2*a)

        print("raiz doble:", raiz)
        print("numero de condicionamiento: infinito")
        return

    r1 = (-b + np.sqrt(discriminante)) / (2*a)
    r2 = (-b - np.sqrt(discriminante)) / (2*a)

    kappa_1 = np.abs(b / (2*a*r1 + b))
    kappa_2 = np.abs(b / (2*a*r2 + b))

    print("primera raiz:", r1)
    print("segunda raiz:", r2)
    print("condicionamiento de la primera raiz:", kappa_1)
    print("condicionamiento de la segunda raiz:", kappa_2)

a = 1
b = -3
c = 2

condicionamiento_b(a, b, c)