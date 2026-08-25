#tarea1.4
suma_total=0
for n in range(0,101):
    for m in range(0,n+1):
       termino=(0.3**n)**m
       suma_total = suma_total + termino
print(f"el resultado es {suma_total}")



