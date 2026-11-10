import numpy as np

def gaussiana(t):
    return np.exp(-t**2/2)/np.sqrt(2*np.pi)

def trapecio(funcion, a, b, n):
    h = (b-a)/n
    puntos = np.linspace(a+h, b-h, n-1)
    return (h/2)*(funcion(a)+2*sum(funcion(puntos))+funcion(b))

def f(p):
    #Aproximé la integral en [0, p] con 1000 subintervalos.
    return trapecio(gaussiana, 0, p, 1000)-0.45

def newton(f,df,p,tolerancia):
    for _ in range(50):
        p_nuevo = p-f(p)/df(p)
        #Comparé el cambio absoluto entre dos iteraciones.
        if abs(p_nuevo-p) < tolerancia:
            return p_nuevo
        p = p_nuevo

    raise Exception("Newton no convergió en 50 iteraciones.")

# La derivada de f es la gaussiana evaluada en p.
x = newton(f, gaussiana, 1.0, 1e-5)
print(f"x = {x:.8f}")