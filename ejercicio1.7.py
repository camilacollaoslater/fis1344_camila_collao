import numpy as np

n = np.arange(1, 101)
resultado = np.sum(np.exp(n) * (n + 1))

print(resultado)