import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def taylor_xsinx(x, n_terminos=10):
    s = np.zeros_like(x, dtype=float)
    for n in range(n_terminos):
        s += (-1)**n * x**(2*n + 2) / factorial(2*n + 1)
    return s

x = np.linspace(-12, 12, 2000)

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(x, x*np.sin(x), color='navy', linestyle='-', lw=2, label=r'$f(x)=x\sin(x)$')
ax.plot(x, taylor_xsinx(x, 10), color='crimson', linestyle='--', lw=2,
        label=r'Taylor, 10 términos (hasta $x^{20}$)')

ax.set_ylim(-12, 14)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.legend(loc='upper center'); ax.grid(alpha=0.3)
plt.show()

for xi in np.arange(1, 12.5, 0.5):
    error = abs(taylor_xsinx(np.array([xi]), 10)[0] - xi*np.sin(xi))
    print(f"x = {xi:4.1f}  error = {error:9.2e}  ->  {'OK' if error < 1e-2 else 'YA NO SIRVE'}")