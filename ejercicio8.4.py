import numpy as np

#Primero calculo cada parte de f con los valores del enunciado.
u = 0.0
v = np.pi / 2
uv = u * v
exp_uv = np.exp(uv)
sen_v = np.sin(v)
producto = u * sen_v
cubo = v**3
suma = exp_uv + producto
f = suma + cubo

print("Valores de los nodos")
nodos = [
    ("u", u), ("v", v),
    ("uv = u * v", uv),
    ("exp_uv = exp(uv)", exp_uv),
    ("sen_v = sin(v)", sen_v),
    ("producto = u * sen_v", producto),
    ("cubo = v**3", cubo),
    ("suma = exp_uv + producto", suma),
    ("f = suma + cubo", f),
]
for nodo, valor in nodos:
    print(f"{nodo:<25} {valor:.10f}")

#Ahora voy hacia atrás desde f. El 1 sale de derivar f respecto de sí misma.
grad_f = 1.0
grad_suma = grad_f
grad_cubo = grad_f
grad_exp_uv = grad_suma
grad_producto = grad_suma
grad_sen_v = grad_producto * u
grad_uv = grad_exp_uv * exp_uv

#Sumo lo que aporta cada camino de u a f y hago lo mismo con v.
grad_u = grad_uv * v + grad_producto * sen_v
grad_v = grad_uv * u + grad_sen_v * np.cos(v) + grad_cubo * 3 * v**2

print(f"\ndf/du = {grad_u:.10f}")
print(f"df/dv = {grad_v:.10f}")