import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np 
import os 
import matplotlib.cm as cm # Para generar colores únicos

# ----------------------------------------------------
# 1. CONFIGURACIÓN E INICIALIZACIÓN
# ----------------------------------------------------

# Directorio donde se encuentran todos los CSV de biomasa
BASE_PATH = '01_data/models_carveme/prokka/biomasas' 

# Encontrar todos los archivos CSV de biomasa
csv_files = glob.glob('01_data/models_carveme/prokka/biomasas/*biomass.csv')

# Diccionario para almacenar los DataFrames cargados (Modelo ID como clave)
ALL_GROWTH_DATA = {} 

print(f"Archivos CSV encontrados: {len(csv_files)}")

# ----------------------------------------------------
# 2. CICLO DE CARGA Y PREPARACIÓN DE DATOS
# ----------------------------------------------------

for file_path in csv_files:
    try:
        df = pd.read_csv(file_path)
        
        # Extraer el ID del modelo (ej: ST00109) del nombre del archivo
        file_name = os.path.basename(file_path)
        # Asume que el ID es todo lo que está antes de '_biomasa.csv'
        model_id = file_name.replace('_biomasa.csv', '') 
        
        # Almacenar el DataFrame
        ALL_GROWTH_DATA[model_id] = df
        
    except Exception as e:
        print(f"Error al cargar {file_name}: {e}")


# ----------------------------------------------------
# 3. CICLO DE PLOTEO AUTOMATIZADO
# ----------------------------------------------------

if len(ALL_GROWTH_DATA) == 0:
    print("ADVERTENCIA: No se pudo cargar ningún dato para graficar.")
    exit()

plt.figure(figsize=(10, 6))

# Definir el eje de tiempo fijo (basado en la longitud del primer DataFrame)
primer_df = list(ALL_GROWTH_DATA.values())[0] 
NUM_ROWS = len(primer_df)
tiempo = np.arange(NUM_ROWS) 

# Preparar un mapa de colores para asignar un color distinto a cada línea
colores = cm.get_cmap('viridis', len(ALL_GROWTH_DATA))
color_index = 0

# Itera sobre el diccionario para graficar CADA MODELO
for model_id, df in ALL_GROWTH_DATA.items():
    
    # Extraer la biomasa (eje Y) y calcular el logaritmo
    #masa = df['Biomass (gr.)]
    masa = df.iloc[:, 1]
    log_masa = np.log(masa + 1e-10) # Log-transformado para el crecimiento

    # Plotea la curva
    plt.plot(tiempo, masa, 
             linestyle='-', 
             color=colores(color_index), # Asigna un color único
             label=model_id) 
    
    color_index += 1 # Pasa al siguiente color

# ----------------------------------------------------
# 4. CONFIGURACIÓN FINAL DEL GRÁFICO
# ----------------------------------------------------

plt.title('Curvas de Crecimiento Microbiano (Escala Logarítmica)')
plt.xlabel('Tiempo (Ciclos de Simulación)')
plt.ylabel('Biomasa [ln(g)]')
plt.grid(True, linestyle='--', alpha=0.6)
# Muestra la leyenda con todos los IDs de los modelos
plt.legend(title='Modelo ID', bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.show()