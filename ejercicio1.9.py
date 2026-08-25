import numpy as np
import matplotlib.pyplot as plt

datos = np.array([0.9, 2.0, 3.6, 5.6, 8.0, 10.9, 14.2, 18.0])

datos_7 = np.array(
    [0.3, 1.7, 4.1, 5.7, 8.5, 10.7, 13.6, 17.2]
)

t = np.arange(1, len(datos) + 1)
error = 0.4  # 4 mm = 0,4 cm

plt.figure(figsize=(10, 6))

# Estudiante con nota 1.0
plt.errorbar(
    t,
    datos,
    yerr=error,
    fmt="o-",
    color="red",
    ecolor="red",
    capsize=5,
    label="Estudiante nota 1.0"
)

# Estudiante con nota 7.0
plt.errorbar(
    t,
    datos_7,
    yerr=error,
    fmt="s--",
    color="blue",
    ecolor="blue",
    capsize=5,
    label="Estudiante nota 7.0"
)

plt.xlabel("Número de medición")
plt.ylabel("Posición (cm)")
plt.title("Comparación de las mediciones con barras de error")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()