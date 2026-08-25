#Tarea 1.1
#Use Python como una calculadora para calcular cuál es la velocidad inicial de una bola que cae una distancia de 2 metros en 0.3 segundos.
#distancia
d = 2
#tiempo
t = 0.3
#gravedad
g = 9.8
#formula para obtener la velocidad inicial
vi = (d-0.5*g*t**2)/t
print(f"la velocidad inicial es :{vi} m/s")