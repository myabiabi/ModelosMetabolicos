import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# --- 1. DATOS DE EJEMPLO ---
# Usamos el DataFrame completo, pero solo seleccionaremos Cepa A y Cepa B.
data = {
    'Valor': [20, 22, 25, 23, 27,   # Cepa A
              15, 18, 17, 19, 16,   # Cepa B
              30, 32, 35, 31, 34],  # Cepa C (no utilizada en Wilcoxon)
    'Grupo': ['Cepa A', 'Cepa A', 'Cepa A', 'Cepa A', 'Cepa A',
              'Cepa B', 'Cepa B', 'Cepa B', 'Cepa B', 'Cepa B',
              'Cepa C', 'Cepa C', 'Cepa C', 'Cepa C', 'Cepa C']
}
df = pd.DataFrame(data)

# --- 2. PREPARACIÓN Y PRUEBA DE WILCOXON RANK-SUM (Mann-Whitney U) ---

# Aísla los dos grupos que deseas comparar
grupo_A = df['Valor'][df['Grupo'] == 'Cepa A'].values
grupo_B = df['Valor'][df['Grupo'] == 'Cepa B'].values

# Ejecutar la prueba
# 'mannwhitneyu' devuelve el estadístico U y el valor p
U_statistic, p_value = stats.mannwhitneyu(grupo_A, grupo_B, alternative='two-sided')

print("--- Resultado de la Prueba de Wilcoxon Rank-Sum (Mann-Whitney U) ---")
print(f"Estadístico U: {U_statistic:.4f}")
print(f"Valor p: {p_value:.4f}")
print("-" * 55)

# Interpretación
alpha = 0.05
if p_value < alpha:
    print("El valor p es menor que 0.05. Se rechaza H0.")
    print("Hay diferencias estadísticamente significativas entre las medianas de Cepa A y Cepa B.")
else:
    print("El valor p es mayor que 0.05. No se rechaza H0.")
    print("No hay diferencias estadísticamente significativas entre las medianas de Cepa A y Cepa B.")


# --- 3. GRÁFICO BOXPLOT CON MATPLOTLIB ---

# Preparamos solo los datos que vamos a plotear
datos_a_plotear = [grupo_A, grupo_B]
nombres_a_plotear = ['Cepa A', 'Cepa B']

plt.figure(figsize=(6, 6))

# Generar el boxplot
plt.boxplot(datos_a_plotear, 
            labels=nombres_a_plotear,
            patch_artist=True,
            medianprops={'color': 'black'},
            boxprops={'facecolor': 'lightcoral', 'edgecolor': 'darkred'})

# Opcional: Plotear los puntos individuales (similar al strip plot de Seaborn)
x = np.array([1] * len(grupo_A) + [2] * len(grupo_B))
y = np.concatenate([grupo_A, grupo_B])
plt.scatter(x, y, color='darkred', alpha=0.6, marker='o', s=50, zorder=3)


# Añadir el resultado p al gráfico
plt.title('Comparación de Valores (Cepa A vs Cepa B)')
plt.ylabel('Valor de Crecimiento/Metabolito')

# Etiqueta para el resultado p
plt.text(1.5, df['Valor'].max() * 1.1, 
         f'Mann-Whitney U: p={p_value:.3e}', 
         ha='center', fontsize=10, 
         bbox=dict(facecolor='white', alpha=0.5))

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()