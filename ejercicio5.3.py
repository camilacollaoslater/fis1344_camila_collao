import numpy as np

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
frecuencias = np.array([12.53, 1.42, 4.68, 5.86, 13.68, 0.69, 1.01, 0.70, 6.25,
    0.44, 0.02, 4.97, 3.15, 6.71, 0.31, 8.68, 2.51, 0.88,
    6.87, 7.98, 4.63, 3.93, 0.90, 0.01, 0.22, 0.90, 0.52])

total_frecuencias = sum(frecuencias)
p = frecuencias / total_frecuencias
H_espanol = -sum(p * np.log(p)) / np.log(2)

poema = """Entre menesteres, el ser envejece,
teje redes, perece
reverdece en el refleje breve
de este presente. Cede."""

poema = poema.lower()
conteos = np.zeros(len(alfabeto), dtype=int)

for i in range(len(alfabeto)):
    for caracter in poema:
        if caracter == alfabeto[i]:
            conteos[i] = conteos[i] + 1

total_letras = sum(conteos)
q = conteos / total_letras

H_poema = 0
for probabilidad in q:
    if probabilidad > 0:
        H_poema = H_poema - probabilidad * np.log(probabilidad) / np.log(2)

cantidad_e = conteos[4]
cantidad_otras = total_letras - cantidad_e
bits_poema = cantidad_e + 5 * cantidad_otras
R_poema = bits_poema / total_letras

print(f"Entropia del español: {H_espanol:.6f} bits por letra")
print(f"Entropia del poema: {H_poema:.6f} bits por letra")
print(f"Compresion del poema: {bits_poema} bits, {R_poema:.6f} bits por letra.")
print(f"La e es la unica vocal y aparece {cantidad_e} de {total_letras} veces.")
print("El poema tiene menor entropia que la distribucion general del español.")
print("Esto permite mayor compresion: menos bits por letra.")

# Nota: 6.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 0/1; claridad: 1/1.
# Faltan comentarios que expliquen los pasos del cálculo de las probabilidades, las entropías y la compresión.
