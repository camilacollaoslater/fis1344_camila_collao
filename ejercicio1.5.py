#tarea1.5
import math
e_real=math.exp(1)
n=0
e_aprox=0
error=999

print(f"el error antes de entrar al while es ´{error}")
while error >= 0.01:
    e_aprox=e_aprox+1/math.factorial(n)
    print(f"el e aprox en la iteracion {n} es {e_aprox}")
    error= abs(e_real-e_aprox)
    print(f"el error en la iteracion {n} es {error}")
    n=n+1

print(f"la aproximacion es {e_aprox}")
print(f"el valor real de e es {e_real}")
print(f"el error final es {error}")
