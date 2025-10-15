import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np 
# --------------------------
# ... (Inicialización de variables: all_models, sim_params, etc.)
initial_mass = [0, 0, 1e-8]   
output_csv_folder = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/prokka/summary'
os.makedirs(output_csv_folder, exist_ok=True)


# --- CICLO PRINCIPAL (CORREGIDO) ---
for model_path in path_list:
    
    file_name = os.path.basename(model_path)
    model_id = file_name.replace('.xml', '') 
    if '-draft' in file_name:
        continue
    
    final_models = None # Reset de variable
    
    try:                                 
        # --- CARGA Y CONFIGURACIÓN (ASUMIDO CORRECTO) ---
        cobra_models = cobra.io.read_sbml_model(model_path)
        processed_models = c.model(cobra_models) 
        all_models[model_id] = processed_models
        
        processed_models.initial_pop = initial_mass
        test_tube = c.layout()
        test_tube.add_model(processed_models)
        
        # B. APLICACIÓN DEL MEDIO (Bloque de set_specific_metabolite y trazas)
        # ... (Toda la configuración del medio debe ir aquí) ...
        
        # C. EJECUCIÓN DE LA SIMULACIÓN
        experimet = c.comets(test_tube, sim_params)
        experimet.run()
        final_models = experimet.total_biomass











        # ----------------------------------------------------
        # VERIFICACIÓN DE ÉXITO Y REGISTRO
        # ----------------------------------------------------
        #if final_models is not None:
            # A. Extracción de valores
            #biomasa_final_valor = final_models['Biomass (gr.)'].iloc[-1]
            
            # B. Registro en el resumen
            #if initial_models == initial_mass:
                #summary = {
                    #'ID': model_id,
                    #'Biomasa_Inicial': initial_models[2], 
                    #'Biomasa_Final_g' : biomasa_final_valor
                #}
                #model_summary_data.append(summary)
            
            # C. EXPORTACIÓN E IMPRESIÓN DE SERIE DE TIEMPO
            #csv_file_name = f"{model_id}_biomasa.csv"
            #csv_output_path = os.path.join(output_csv_folder, csv_file_name)
            #final_models.to_csv(csv_output_path, index=False)
            
            #print(f"ÉXITO: {model_id} registrado y Serie de Tiempo guardada en {csv_file_name}")
            #print(f"\n---CRECIMIENTO {model_id}---")
            #print(final_models.to_string()) # Imprime la tabla completa
        #else:
            # 3. CAPTURA DE MODELOS INVIABLES
            #print(f"ADVERTENCIA (Inviable): Modelo {model_id} falló la simulación Batch (resultado = None).")
            

    #except Exception as e:
        # Este except es necesario y debe estar alineado con el try
        #print(f"ERROR CRÍTICO: Falló el procesamiento de {model_id}: {e}. Archivo: {file_name}")

    #finally:
        # El finally se ejecuta siempre, pero no hay necesidad de imprimir la tabla aquí.
        #pass
        
# --- IMPRESIÓN DEL RESUMEN FINAL (FUERA DEL BUCLE) ---
# ... (Bloque final de impresión) ...