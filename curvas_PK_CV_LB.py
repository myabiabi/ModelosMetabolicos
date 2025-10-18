# ----------------------------------------------------
# Cargar paquetes
import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np 
import os 
import matplotlib.cm as cm 
# ----------------------------------------------------
# Crear variables
# Directorio donde se encuentran todos los CSV de biomasa
BASE_PATH = '01_data/models_carveme/prokka/biomasas' 
# Encontrar todos los archivos CSV de biomasa
csv_files = glob.glob('01_data/models_carveme/prokka/biomasas/*biomass.csv')
# Diccionario para almacenar los DataFrames cargados (Modelo ID como clave)
ALL_GROWTH_DATA = {} 
colores_bac = {
    # Rojo/Marrón (Top 5 del póster)
    'ST00060': '#D4807C', # Arthrobacter
    #'ST00160': '#C76662', # Rhodococcus #❌
    #'ST00116': '#B7464C', # Variovorax #❌
    'ST00164': '#9E3345', # Ballicus thuringesis #🤔
    'ST00143': '#752530', # Paenibacillus
    # Azul/Cian (Bottom 5 del póster)
    'ST00042': '#80B6B3', # Pseudomonas umsongensis #🤔
    'ST00101': '#5F9EAD', # Pseudomonas
    'ST00109': '#3D788E', # Mycobacterium
    'ST00154': '#26526B', # Agrobacterium
    'ST00046': '#1A3749'  # Bacillus (Usando el color más oscuro de la escala azul)
}
name_bac = {
    'ST00060': r'$\it{Arthrobacter\ sp.}$', #✅
    #'ST00160': r'$\it{Rhodococcus\ erythropolis}$', #❌
    #'ST00116': r'$\it{Variovorax\ paradoxus}$', #❌
    'ST00164': r'$\it{Ballicus thuringesis\ sp.}$', #🤔
    'ST00143': r'$\it{Paenibacillus\ sp.}$', #✅
    'ST00042': r'$\it{Pseudomonas umsongensis\ sp.}$', #🤔
    #'ST00101': r'$\it{Pseudomonas\ sp.}$', ❌
    'ST00109': r'$\it{Mycobacterium\ sp.}$', #✅
    'ST00154': r'$\it{Agrobacterium\ sp.}$', #✅
    'ST00046': r'$\it{Bacillus\ sp.}$', #✅
}

print(f"Archivos CSV encontrados: {len(csv_files)}")
# ----------------------------------------------------
# Ciclo para cargar todos los datos 
for file_path in csv_files:    
    try:
        df = pd.read_csv(file_path)
        
        # Extraer el ID del modelo 
        file_name = os.path.basename(file_path)
        model_id = file_name.replace('_biomass.csv', '') 

        scientific_name = name_bac.get(model_id)
        final_label = f"{scientific_name} ({model_id})"
        
        # Almacenar el DataFrame
        ALL_GROWTH_DATA[model_id] = df
        
    except Exception as e:
        print(f"Error al cargar {file_name}: {e}")

# -----------------------------------------------------
# Ciclo graficar todas las cuvas 
plt.figure(figsize=(8, 5))

# Definir el eje de tiempo fijo (basado en la longitud del primer DataFrame)
primer_df = list(ALL_GROWTH_DATA.values())[0] 
NUM_ROWS = len(primer_df)
tiempo = np.arange(NUM_ROWS) 

# Preparar un mapa de colores para asignar un color distinto a cada línea
#colores = cm.get_cmap('viridis', len(ALL_GROWTH_DATA))
#color_index = 0

# Itera sobre el diccionario para graficar CADA MODELO
for model_id, df in ALL_GROWTH_DATA.items():
    # Extraer la biomasa (eje Y) y calcular el logaritmo
    #masa = df['Biomass (gr.)]
    masa = df.iloc[:, 1]
    log_masa = np.log(masa + 1e-10) # Log-transformado para el crecimiento
    cepa_color = colores_bac.get(model_id, 'gray') # Busca el color Hex por el ID
    # Plotea la curva
    plt.plot(tiempo, log_masa, 
             linestyle='-', 
             color= cepa_color, # Asigna un color único
             label=model_id) 
    
    #color_index += 1 # Pasa al siguiente color

# ----------------------------------------------------
# 4. CONFIGURACIÓN FINAL DEL GRÁFICO
# ----------------------------------------------------

plt.title('Curvas de Crecimiento Microbiano (Escala Logarítmica)')
plt.xlabel('Tiempo (Ciclos de Simulación)')
plt.ylabel('Biomasa [ln(g)]')
plt.grid(True, linestyle='--', alpha=0.6)
# Muestra la leyenda con todos los IDs de los modelos
plt.legend(title='Modelo ID', bbox_to_anchor=(1.05, 1), loc='upper right') 
output_folder = '03_graficas'
output_path = os.path.join(output_folder)
plt.savefig(output_path)


plt.show()
