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

# --- CICLO PRINCIPAL ---
for model_path in path_list:
    
    file_name = os.path.basename(model_path)
    model_id = file_name.replace('.xml', '') 
    if '-draft' in file_name:
        continue
    
    # Reiniciar la variable de resultado para cada iteración
    final_models = None # Se inicializa antes del try
    
    try:                                 
        cobra_models = cobra.io.read_sbml_model(model_path)
        processed_models = c.model(cobra_models) 
        all_models[model_id] = processed_models
        
        # A. CONFIGURACIÓN E INICIALIZACIÓN
        processed_models.initial_pop = initial_mass
        test_tube = c.layout()
        test_tube.add_model(processed_models)
        
        # B. APLICACIÓN DEL MEDIO (Asumido como correcto)
        # ... (Todas las líneas test_tube.set_specific_metabolite) ...
        # ... (trace_metabolites loop) ...

        # C. EJECUCIÓN DE LA SIMULACIÓN
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
                print(f"ÉXITO: {model_id} registrado en el resumen.")
        else:
            # Captura modelos que son inviables
            print(f"ADVERTENCIA (Inviable): Modelo {model_id} falló la simulación Batch (resultado = None).")

    
    #except Exception as e:
    #print(f"ERROR CRÍTICO: Falló el procesamiento de {model_id}: {e}. Archivo: {file_name}")

    #finally:
        # --- BLOQUE FINALLY (CORREGIDO) ---
        # Solo intenta imprimir si la simulación fue exitosa (final_models fue asignado y no es None)
        #if final_models is not None:
            #print(f"\n---Crecimiento {model_id}---")
            # CORRECCIÓN: Se añaden los paréntesis a .to_string()
            #print(final_models.to_string()) 
        #else:
            # Imprime el mensaje de advertencia si falló la simulación
            #print(f"--- Iteración {model_id} finalizada. Estado: FALLO DE SIMULACIÓN/NO REGISTRADO ---")

# --- IMPRESIÓN DEL RESUMEN FINAL ---
  
print(f"\nTotal de modelos cargados: {len(all_models)}")   
if model_summary_data:
    final_summary_df = pd.DataFrame(model_summary_data)
    
    print("\n========================================================")
    print("RESUMEN FINAL DE MASAS ASIGNADAS Y VERIFICADAS")
    print("========================================================")
   
    print(final_summary_df.to_string())
    
else:
    print("\nADVERTENCIA: La lista de resumen (model_summary_data) está vacía.")
        #print(f"\n---Crecimiento del modelo {model_id}---")
        #print(experimet.total_biomass.to_string)

#print("\n--- LISTA COMPLETA DE MODELOS CARGADOS DISPONIBLES ---")

# Usamos .keys() para obtener una vista de todas las claves (IDs de los modelos)
#listado_de_ids = list(all_models.keys())

# Imprimir la lista
#print(listado_de_ids)

# Opcional: Imprimir el total para confirmar
#print(f"\nTotal de modelos listados: {len(listado_de_ids)}")




# --- El bucle 'for' continúa aquí con el siguiente modelo ---


        # ----------------------------------------------------
        # BLOQUE DE VERIFICACIÓN Y REGISTRO (CORREGIDO)
        # ----------------------------------------------------

        # 1. VERIFICACIÓN DE VIABILIDAD (final_models NO es None)
        #if final_models is not None:
            
            #biomasa_final_valor = final_models['Biomass (gr.)'].iloc[-1]
            
            # 2. VERIFICACIÓN DE ASIGNACIÓN (Siempre debe ser True, pero se mantiene la verificación)
            #if initial_models == initial_mass:
                #summary = {
                    #'ID': model_id,
                    #'Biomasa_Inicial': initial_models[2],
                    #'Biomasa_Final_g' : biomasa_final_valor
                #}
                # Esta línea debe estar al mismo nivel que 'summary'
                #model_summary_data.append(summary)
                
                #print(f"ÉXITO: Modelo {model_id} registrado. Biomasa Final: {biomasa_final_valor:.4f} g")

        #else:
            # 3. CAPTURA DE MODELOS INVIABLES
            # Este 'else' está alineado con el 'if final_models is not None'
            #print(f"ADVERTENCIA (Inviable): Modelo {model_id} falló la simulación Batch (resultado = None).")
                
    
    #finally:

# --- IMPRESIÓN DEL RESUMEN FINAL (FUERA DEL BUCLE) ---

#print(f"\nTotal de modelos cargados: {len(all_models)}")   
#if model_summary_data:
    #final_summary_df = pd.DataFrame(model_summary_data)
    
    #print("\n========================================================")
    #print("RESUMEN FINAL DE MASAS ASIGNADAS Y VERIFICADAS")
    #print("========================================================")
   
    #print(final_summary_df.to_string())
    
#else:
    #print("\nADVERTENCIA: La lista de resumen (model_summary_data) está vacía.")

# Asumimos que el código de carga ya se ejecutó y llenó all_models.
