import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------------
datos = pd.read_csv('01_data/models_carveme/prokka/biomasas/ST00109_biomass.csv')
datos2 = pd.read_csv('01_data/models_carveme/prokka/biomasas/ST00143_biomass.csv')

print("--- Nombres de las columnas del archivo ST00109 ---")
# Usamos list() para imprimir las columnas como una lista estándar de Python
print(list(datos.columns))

print("\n--- Nombres de las columnas del archivo ST00143 ---")
print(list(datos2.columns))
