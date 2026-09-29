import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb, factorial

def binomial(n, r, p):
    return comb(r, n) * p**n * (1 - p)**(r - n)

def poisson(n, lamda):
    return lamda**n * np.exp(-lamda) / factorial(n)

valores_n = range(11)
valores_r = [10, 50, 100, 1000]

plt.figure(figsize=(9, 6))

for r in valores_r:
    p = 2 / r
    probabilidades = [binomial(n, r, p) for n in valores_n]
    plt.plot(valores_n, probabilidades, 'o-',
             label='Binomial, r = ' + str(r))

probabilidades_poisson = [poisson(n, 2) for n in valores_n]
plt.plot(valores_n, probabilidades_poisson, 'k--',
         label='Poisson, lambda = 2')

plt.xlabel('Numero de detecciones n')
plt.ylabel('Probabilidad P(n)')
plt.title('Distribucion binomial y aproximacion de Poisson')
plt.legend()
plt.show()

print('Poisson se puede usar cuando r es grande y p = 2/r es pequeño,')
print('con ensayos independientes y lambda = r*p = 2')
print('al aumentar r, la distribucion binomial se aproxima a Poisson.')