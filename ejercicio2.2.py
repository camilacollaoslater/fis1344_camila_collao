import numpy as np
#primera función: f(x) = tanh(x)

def kappa_tanh(x):
    if x == 0:
        return 1.0

    return np.abs(2*x / np.sinh(2*x))
print("primera funcion")
print("cerca de cero:", kappa_tanh(0.001))
print("en x = 1:", kappa_tanh(1))
print("en x = 10:", kappa_tanh(10))


#segunda función: f(x) = (exp(x) - 1)/x

def kappa_exponencial(x):
    if x == 0:
        return 0.0

    return np.abs((np.exp(x)*(x - 1) + 1) /(np.exp(x) - 1))
print("segunda funcion")
print("cerca de cero:", kappa_exponencial(0.001))
print("en x = 1:", kappa_exponencial(1))
print("en x = 10:", kappa_exponencial(10))
print("en x = 20:", kappa_exponencial(20))
print("en x = -10:", kappa_exponencial(-10))


#tercera función: f(x) = (1 - cos(x))/x

def kappa_coseno(x):
    if x == 0:
        return 1.0

    return np.abs(x*np.sin(x) /(1 - np.cos(x)) - 1)
print("tercera funcion")
print("cerca de cero:", kappa_coseno(0.001))
print("en x = pi:", kappa_coseno(np.pi))
print("en x = 3*pi:", kappa_coseno(3*np.pi))

# no se evalua en 2*pi porque el denominador es cero.
distancia = 0.001
print("cerca de 2*pi por la izquierda:", kappa_coseno(2*np.pi - distancia))
print("cerca de 2*pi por la derecha:", kappa_coseno(2*np.pi + distancia))
print("cerca de -2*pi:", kappa_coseno(-2*np.pi + distancia))