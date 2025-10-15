import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np 
# --------------------------
all_models = {} 
sim_params = c.params()
path_list = glob.glob('01_data/models_carveme/prokka/lb/ST*.xml')
model_summary_data = [] 
initial_mass = [0, 0, 1e-8]   

# --- 1. CONFIGURACIÓN DE RUTA ABSOLUTA (CRUCIAL PARA EL GUARDADO) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_CSV_FOLDER = os.path.join(BASE_DIR, '01_data/models_carveme/prokka/summary')
os.makedirs(OUTPUT_CSV_FOLDER, exist_ok=True)
print(f"Directorio de CSV creado/verificado: {OUTPUT_CSV_FOLDER}")
# ------------------------------------------

# --- CICLO PRINCIPAL (LÓGICA DE SIMULACIÓN Y REGISTRO) ---
for model_path in path_list:
    
    file_name = os.path.basename(model_path)
    model_id = file_name.replace('.xml', '') 
    if '-draft' in file_name:
        continue
    
    final_models = None 
    
    try:                                 
        # ... (Carga de modelo y configuración de medio) ...
        # Se asume que todas las líneas de configuración del medio son correctas
        
        experimet = c.comets(test_tube, sim_params)
        experimet.run()
        final_models = experimet.total_biomass
        initial_models = processed_models.initial_pop 


        if final_models is not None:
            biomasa_final_valor = final_models['Biomass (gr.)'].iloc[-1]
            if initial_models == initial_mass:
                summary = {
                    'ID': model_id,
                    'Biomasa_Inicial': initial_models[2], 
                    'Biomasa_Final_g' : biomasa_final_valor
                }
                model_summary_data.append(summary)
                
                # --- PUNTO CRÍTICO DE GUARDADO ---
                csv_file_name = f"{model_id}_biomasa.csv"
                csv_output_path = os.path.join(OUTPUT_CSV_FOLDER, csv_file_name)
                
                # EL GUARDADO DEBE FUNCIONAR AHORA
                final_models.to_csv(csv_output_path, index=False)
                
                print(f"ÉXITO: {model_id} registrado y Serie de Tiempo guardada en {csv_output_path}")

        # ... (El resto del código de manejo de errores e impresión final) ...