import numpy as np
#datos
qmax = 0.1
N = 500000
dq = qmax / N

i = np.arange(1, N + 1)
q = i * dq

# integrales calculadas por separado
I1 = dq * np.sum(q**2 * (1/q**5 + 3/q))
I2 = dq * np.sum(q**2 * (-1/q**5 + 1/q))

print("I1 =", I1)
print("I2 =", I2)
print("I1 + I2 =", I1 + I2)

#integral despues de sumar los integrandos
I = dq * np.sum(q**2 * (4/q))
print("integral simplificada =", I)

#resultado exacto
I_exacto = 2 * qmax**2
print("resultado exacto =", I_exacto)