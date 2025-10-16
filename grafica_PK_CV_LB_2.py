import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import numpy as np
# --------------------------
# 1. CARGAR PAQUETES Y VARIABLES GLOBALES
# --------------------------
NUM_CYCLE = 100
# CORRECCIÓN 1: Inicializamos como Diccionario {} para usar IDs como claves
ALL_MODELS_DATA = {} 
print("Iniciando carga de DataFrames.")
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


# 3. ACCESO A DATOS, PREPARACIÓN DE TIEMPO Y PLOTEO
if len(ALL_MODELS_DATA) > 0:
    
    plt.figure(figsize=(10, 6))
    
    # CORRECCIÓN 3: Acceder al primer DataFrame (un valor del diccionario) para definir el tiempo
    # Usamos .values() para obtener los DataFrames, y [0] para el primero.
    primer_df = list(ALL_MODELS_DATA.values())[0] 
    
    # Definir el eje de tiempo fijo
    cycles = len(primer_df)
    tiempo = np.arange(cycles) 
    
    print(f"Total de modelos cargados y listos para graficar: {len(ALL_MODELS_DATA)}")
    print(f"Longitud de la simulación (ciclos): {cycles}")

    # 4. CICLO PARA GRAFICAR TODAS LAS CURVAS
    # Usamos .items() para obtener el ID (clave) y el DataFrame (valor)
    for model_id, df in ALL_MODELS_DATA.items():
        
        # CORRECCIÓN 4: Acceder a la columna de Biomasa por su nombre (no por el ID del archivo)
        # Se asume que la columna es 'Biomass (gr.)'
        masa = df['Biomass (gr.)'] 
        
        # Calculamos el logaritmo para la gráfica científica
        log_masa = np.log(masa + 1e-10) 

        # Ploteamos: Eje X (Tiempo) vs Eje Y (Log-Masa)
        plt.plot(tiempo, log_masa, label=model_id)

    # 5. CONFIGURACIÓN FINAL DEL GRÁFICO
    plt.title('Curvas de Crecimiento Bacteriano (Log-transformado)')
    plt.xlabel('Tiempo (Ciclos de Simulación)')
    plt.ylabel('Biomasa [ln(g)]')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(title='Modelo ID', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

else:
    print("ADVERTENCIA: No se pudo cargar ningún DataFrame para ploteo.")





















#import pandas as pd
#import matplotlib.pyplot as plt
#import glob

#csv_file_1 = glob.glob('01_data/models_carveme/prokka/biomasas/ST00109_biomass.csv')
#csv_file_2 = glob.glob('01_data/models_carveme/prokka/biomasas/ST00143_biomass.csv')


#all_dataframes = []
#for file in csv_files:
        #df = pd.read_csv(file)
        #all_dataframes.append(df)
#print(all_dataframes)





#import numpy as np
#from scipy.integrate import odeint
#import matplotlib.pyplot as plt

# Example: Simple competitive growth model for two bacterial strains
#def bacterial_community_growth(N, t, r1, K1, r2, K2, alpha12, alpha21):
    #N1, N2 = N # Population sizes of strain 1 and strain 2
    
    # Logistic growth with competitive inhibition
    ##dN1dt = r1 * N1 * (1 - (N1 + alpha12 * N2) / K1)
    #dN2dt = r2 * N2 * (1 - (N2 + alpha21 * N1) / K2)
    
    #return [dN1dt, dN2dt]

# Parameters
#r1, K1 = 0.5, 1000 # Growth rate and carrying capacity for strain 1
#r2, K2 = 0.4, 800  # Growth rate and carrying capacity for strain 2
#alpha12 = 0.8     # Effect of strain 2 on strain 1
#alpha21 = 0.6     # Effect of strain 1 on strain 2

#initial_populations = [10, 5] # Initial populations of N1 and N2
#time_points = np.linspace(0, 50, 500) # Time points for simulation

# Solve the differential equations
#solution = odeint(bacterial_community_growth, initial_populations, time_points, 
                   #args=(r1, K1, r2, K2, alpha12, alpha21))

# Extract individual strain populations
#N1_history = solution[:, 0]
#N2_history = solution[:, 1]
#Total_N = N1_history + N2_history

# Plotting the growth curves
#plt.figure(figsize=(10, 6))
#plt.plot(time_points, N1_history, label='Strain 1 Population')
#plt.plot(time_points, N2_history, label='Strain 2 Population')
#plt.plot(time_points, Total_N, label='Total Community Population', linestyle='--')
#plt.xlabel('Time')
#plt.ylabel('Population Size')
#plt.title('Bacterial Community Growth Curve')
#lt.legend()
#plt.grid(True)
#plt.show()