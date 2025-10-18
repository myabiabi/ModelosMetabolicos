# Cargar paquetes 
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import numpy as np
# --------------------------
# Variables
# --------------------------
NUM_CYCLE = 100
ALL_MODELS_DATA = {} 
# -----------------------------------

# 2. CARGA DE DATOS Y REGISTRO EN DICCIONARIO
csv_files = glob.glob('01_data/models_carveme/prokka/biomasas/*biomass.csv')
print(f"Número de archivos CSV encontrados: {len(csv_files)}")

for file_path in csv_files:
    try:
        df = pd.read_csv(file_path)
        
        # Extraer el ID del modelo (STxxxx)
        file_name = os.path.basename(file_path)
        # Limpiamos el nombre para usarlo como clave
        model_id = file_name.replace('_biomass.csv', '') 
        
        # CORRECCIÓN 2: Almacenamos el DataFrame en el diccionario con el ID como clave
        ALL_MODELS_DATA[model_id] = df
        
    except Exception as e:
         print(f"ERROR: Fallo al cargar {file_name}: {e}")

# ----------------------------------------------
