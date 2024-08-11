import numpy as np

# Parámetros de la función logística
t = np.arange(1, 41)  # Años del 1 al 40
t_0 = 20  # Punto medio del crecimiento
k = 0.30  # Tasa de crecimiento

# Función logística
P = 1 / (1 + np.exp(-k * (t - t_0)))

# Normalización para que la suma sea 100%
P_normalized = P / P.sum() * 100

# Verificamos que la suma sea 100%
P_normalized_sum = P_normalized.sum()

for item in P_normalized:
    print(item)
