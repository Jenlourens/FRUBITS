import pandas as pd
import numpy as np

# Leer el archivo csv
df = pd.read_csv('tiempos-maquinas.csv', delimiter=',', decimal='.')

# Convertir el DataFrame a una matriz
matrix = df.values

# Número de trabajos - Número de filas
num_jobs = matrix.shape[0]

# Número de máquinas - Número de columnas
num_machines = matrix.shape[1]

# Inicializar variables
tiempos_acumulados = [0] * num_machines
secuencia_optima = []
tiempos_maquina = [0] * num_machines
tiempo_total = 0

# Aplicar la regla SPT
while len(secuencia_optima) < num_jobs:
  # Encontrar el trabajo con el menor tiempo de procesamiento total
  min_tiempo_total = float('inf')
  min_indice_trabajo = -1
  for i in range(num_jobs):
    if i not in secuencia_optima:
      tiempo_total = np.sum(matrix[i])
      if tiempo_total < min_tiempo_total:
        min_tiempo_total = tiempo_total
        min_indice_trabajo = i

  # Agregar el trabajo a la secuencia óptima
  secuencia_optima.append(min_indice_trabajo)

  # Actualizar los tiempos acumulados
  for j in range(num_machines):
    tiempos_acumulados[j] += matrix[min_indice_trabajo][j]

  # Calcular el makespan (tiempo de finalización del último trabajo)
  makespan = max(tiempos_acumulados)

  # Calcular el tiempo promedio por máquina
  for j in range(num_machines):
    tiempos_maquina[j] += matrix[min_indice_trabajo][j]

  # Calcular el tiempo total
  tiempo_total = np.sum(tiempos_maquina)

# Imprimir resultados
print("Secuencia óptima:", secuencia_optima)
print("Makespan:", makespan)
print("Tiempo promedio por máquina:", tiempos_maquina)
print("Tiempo total:", tiempo_total)