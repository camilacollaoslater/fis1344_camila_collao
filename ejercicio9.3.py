import numpy as np
class MinStep(Exception):
    pass
def rkf(f, a, b, yo, tol, hmin, hmax, orden=4):
    t, w, h = a, yo, hmax
    ts, sol = [t], [w]

    while t < b:
        h = min(h, b - t)

        k1 = h*f(t,w)
        k2 = h*f(t + h/4, w + k1/4)
        k3 = h*f(t + 3*h/8, w + 3*k1/32 + 9*k2/32)
        k4 = h*f(t + 12*h/13,
                 w + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
        k5 = h*f(t + h,
                 w + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
        k6 = h*f(t + h/2,
                 w - 8*k1/27 + 2*k2 - 3544*k3/2565
                 + 1859*k4/4104 - 11*k5/40)

        #Estimamos el error
        R = abs(k1/360 - 128*k3/4275 - 2197*k4/75240
                + k5/50 + 2*k6/55)

        if R <= tol:
            # Elegimos la solución
            if orden == 4:
                w = w + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5
            else:
                w = (w + 16*k1/135 + 6656*k3/12825
                     + 28561*k4/56430 - 9*k5/50 + 2*k6/55)

            t = t + h
            ts.append(t)
            sol.append(w)

        if t >= b:
            break

        #Ajustamos el tamaño del siguiente paso.
        if R == 0:
            q = 4
        else:
            q = 0.84*(tol/R)**(1/4)

        h = min(hmax, h*max(0.1, min(q, 4)))

        if t + h > b:
            h = b - t
        elif h < hmin:
            raise MinStep('Se excedió el paso mínimo.')

    return np.array(ts), np.array(sol)


def f(t, y):
    return (2 - 2*t*y)/(t**2 + 1)


def exacta(t):
    return (2*t + 1)/(t**2 + 1)


print('Orden y(3) Error maximo en los puntos calculados')
for orden in [4, 5]:
    t, y = rkf(f, 0, 3, 1, 1e-6, 0.01, 0.25, orden)
    error = abs(y - exacta(t))
    print(f'{orden} {y[-1]:.10f}  {error.max():.3e}')

print("La de orden 5 tiene menos error en este problema.")
print("Se usa la de orden 4 porque la diferencia entre ambas permite estimar" 
      "su error y ajustar el paso. Esa diferencia no estima directamente"
      "el error de la de orden 5.")