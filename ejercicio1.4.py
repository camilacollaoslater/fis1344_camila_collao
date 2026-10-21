#tarea1.4
suma_total=0
for n in range(0,101):
    for m in range(0,n+1):
       termino=(0.3**n)**m
       suma_total = suma_total + termino
print(f"el resultado es {suma_total}")

# Nota: 6.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 0/1; claridad: 1/1.
# Faltan comentarios que expliquen la inicialización, los ciclos anidados y la acumulación de la suma.
