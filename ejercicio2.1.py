import numpy as np
#datos
kappa = 1e6
error_experimental = 1e-6

#calculo con 64 bits
epsilon_64 = np.finfo(np.float64).eps
error_64 = kappa * epsilon_64

print("epsilon de 64 bits:", epsilon_64)
print("error con 64 bits:", error_64)
print("error experimental:", error_experimental)
print("¿se puede comparar usando 64 bits?", error_64 < error_experimental)

#calculo con 32 bits
epsilon_32 = np.finfo(np.float32).eps
error_32 = kappa * epsilon_32

print("epsilon de 32 bits:", epsilon_32)
print("error con 32 bits:", error_32)
print("error porcentual con 32 bits:", error_32 * 100, "%")
print("¿se puede comparar usando 32 bits?", error_32 < error_experimental)