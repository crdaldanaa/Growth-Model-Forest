import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo de Chapman-Richards
K = 100  # Tamaño máximo (capacidad de carga)
r = 0.1  # Tasa de crecimiento
b = 5  # Parámetro de forma

# Función de crecimiento de Chapman-Richards


def chapman_richards(t, K, r, b):
    return K * (1 - np.exp(-r * t))**b


# Calcular el crecimiento para 40 años
años = np.arange(1, 41)
crecimiento = chapman_richards(años, K, r, b)

# Normalizar los valores para que la suma sea 100%
crecimiento_normalizado = crecimiento / crecimiento.sum() * 100

# Mostrar los valores porcentuales
print("Valores porcentuales anuales:")
for i, valor in enumerate(crecimiento_normalizado, start=1):
    print(valor)

# Graficar el crecimiento
plt.plot(años, crecimiento_normalizado, marker='o')
plt.title('Crecimiento porcentual anual del bosque (Chapman-Richards)')
plt.xlabel('Años')
plt.ylabel('Crecimiento porcentual (%)')
plt.grid(True)
plt.show()
