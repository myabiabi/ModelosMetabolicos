import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np 
import csv
# --------------------------
all_models = {} 
sim_params = c.params()
path_list = glob.glob('01_data/models_carveme/prokka/lb/ST*.xml')
model_summary_data = [] 
initial_mass = [0, 0, 1e-8]   

#output_csv_folder = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/prokka/summary'
#os.makedirs(output_csv_folder, exist_ok=True)


# --- CICLO PRINCIPAL ---
for model_path in path_list:
    
    file_name = os.path.basename(model_path)
    model_id = file_name.replace('.xml', '') 
    if '-draft' in file_name:
        continue
    
    # Reiniciar la variable de resultado para cada iteración
    #map(list, list)
    final_models = None # Se inicializa antes del try
    
    try:                                 
        cobra_models = cobra.io.read_sbml_model(model_path)
        processed_models = c.model(cobra_models) 
        all_models[model_id] = processed_models
        
        # A. CONFIGURACIÓN E INICIALIZACIÓN
        processed_models.initial_pop = initial_mass
        test_tube = c.layout()
        test_tube.add_model(processed_models)

        test_tube.set_specific_metabolite("h2o_e", 100)
        test_tube.set_specific_metabolite("o2_e", 10)
        test_tube.set_specific_metabolite("pi_e", 100)
        test_tube.set_specific_metabolite("prbamp_e", 100)
        test_tube.set_specific_metabolite("glu__L_e", 1)
        test_tube.set_specific_metabolite("mn2_e", 100)
        test_tube.set_specific_metabolite("gly_e", 1)
        test_tube.set_specific_metabolite("zn2_e", 100)
        test_tube.set_specific_metabolite("ala__L_e", 1)
        test_tube.set_specific_metabolite("lys__L_e", 1)
        test_tube.set_specific_metabolite("asp__L_e", 1)
        test_tube.set_specific_metabolite("so4_e", 1)
        test_tube.set_specific_metabolite("arg__L_e", 1)
        test_tube.set_specific_metabolite("ser__L_e", 1)
        test_tube.set_specific_metabolite("cu2_e", 1)
        test_tube.set_specific_metabolite("met__L_e", 1)
        test_tube.set_specific_metabolite("trp__L_e", 1)
        test_tube.set_specific_metabolite("phe__L_e", 1)
        test_tube.set_specific_metabolite("h_e", 1)
        test_tube.set_specific_metabolite("tyr__L_e", 1)
        test_tube.set_specific_metabolite("cys__L_e", 1)
        test_tube.set_specific_metabolite("ura_e", 1)
        test_tube.set_specific_metabolite("cl_e", 1)
        test_tube.set_specific_metabolite("leu__L_e", 1) 
        test_tube.set_specific_metabolite("his__L_e", 1)
        test_tube.set_specific_metabolite("pro__L_e", 1)
        test_tube.set_specific_metabolite("cobalt2_e", 100)
        test_tube.set_specific_metabolite("val__L_e", 1)
        test_tube.set_specific_metabolite("thr__L_e", 1)
        test_tube.set_specific_metabolite("adn_e", 0.1)
        test_tube.set_specific_metabolite("thymd_e", 0.1)
        test_tube.set_specific_metabolite("k_e", 100)
        test_tube.set_specific_metabolite("h2s_e", 0.1)
        test_tube.set_specific_metabolite("ins_e", 0.1)
        test_tube.set_specific_metabolite("uri_e", 0.1)
        test_tube.set_specific_metabolite("mg2_e", 100)
        test_tube.set_specific_metabolite("gsn_e", 0.1)
        test_tube.set_specific_metabolite("ile__L_e", 1)
        test_tube.set_specific_metabolite("cys__L_e", 1)
        test_tube.set_specific_metabolite("skm_e", 1)
        test_tube.set_specific_metabolite("fol_e", 1)
        test_tube.set_specific_metabolite("dadn_e", 1)
        test_tube.set_specific_metabolite("lipoate_e", 0.1)
        test_tube.set_specific_metabolite("na1_e", 100)
        test_tube.set_specific_metabolite("cd2_e", 100)
        test_tube.set_specific_metabolite("aso4_e", 100)
        test_tube.set_specific_metabolite("fe2_e", 100)
        test_tube.set_specific_metabolite("fe3_e", 100)
        test_tube.set_specific_metabolite("cro4_e", 100)
        test_tube.set_specific_metabolite("nh3_c_e", 100)
        test_tube.set_specific_metabolite("pheme_e", 100)
        test_tube.set_specific_metabolite("cmp_e", 100)
        test_tube.set_specific_metabolite("ump_e", 100)
        test_tube.set_specific_metabolite("gmp_e", 100)
        test_tube.set_specific_metabolite("pydx_e", 100)
        test_tube.set_specific_metabolite("nac_e", 100)
        test_tube.set_specific_metabolite("ribflv_e", 100)
        test_tube.set_specific_metabolite("pphn_e", 100)
        test_tube.set_specific_metabolite("hxan_e", 100)
        test_tube.set_specific_metabolite("thmpp_e", 0.1)
        test_tube.set_specific_metabolite("cbl1_e", 0.1)

        # Add typical trace metabolites and oxygen coli as static
        trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                            'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

        for i in trace_metabolites:
            test_tube.set_specific_metabolite(i, 1000)
            test_tube.set_specific_static(i, 1000)
        # C. EJECUCIÓN DE LA SIMULACIÓN
        experimet = c.comets(test_tube, sim_params)
        experimet.run()
        final_models = experimet.total_biomass
        initial_models = processed_models.initial_pop 


        if final_models is not None:

            #biomasa_final_valor = final_models['Biomass (gr.)'].iloc[-1]
            #if initial_models == initial_mass:
                #summary = {
                    #'ID': model_id,
                    #'Biomasa_Inicial': initial_models[2], 
                    #'Biomasa_Final_g' : biomasa_final_valor
                #}
                #model_summary_data.append(summary)

                #path = f"{output_csv_folder}/{model_id}_biomasa.csv"
                #csv_output_path = #os.path.join(output_csv_folder, csv_file_name)
                #final_models.to_csv(csv_output_path, index=False)
                #print(f"ÉXITO: {model_id} registrado y Serie de Tiempo guardada en {csv_file_name}")
                

        #else:
            print(f"ADVERTENCIA (Inviable): Modelo {model_id} falló la simulación Batch (resultado = None).")

    #except Exception as e:
        print(f"ERROR CRÍTICO: Falló el procesamiento de {model_id}: {e}. Archivo: {file_name}")


    #finally:
        # --- BLOQUE FINALLY (CORREGIDO) ---
        # Solo intenta imprimir si la simulación fue exitosa (final_models fue asignado y no es None)
        #if final_models is not None:
            #print(f"\n---Crecimiento {model_id}---")
            # CORRECCIÓN: Se añaden los paréntesis a .to_string()
            #print(final_models.to_string()) 
        #else:
            # Imprime el mensaje de advertencia si falló la simulación
            #"print(f"--- Iteración {model_id} finalizada. Estado: FALLO DE SIMULACIÓN/NO REGISTRADO ---")




# --- IMPRESIÓN DEL RESUMEN FINAL ---
  
print(f"\nTotal de modelos cargados: {len(all_models)}")   
if model_summary_data:
    final_summary_df = pd.DataFrame(model_summary_data)

    #out_folder = '01_data/summary'
    #csv_output_path = os.path.join('01_data/summary', f'{model_id}_biomass.csv')
    #os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)
    #final_summary_df.to_csv(csv_output_path, index=False)
    
    print("\n========================================================")
    print("RESUMEN FINAL DE MASAS ASIGNADAS Y VERIFICADAS")
    print("========================================================")
   
    print(final_summary_df.to_string()) 
    
else:
    print("\nADVERTENCIA: La lista de resumen (model_summary_data) está vacía.")

##llamar final_summary_df



##############f final_models is not None:
            
            # --- IMPRESIÓN DE LA TABLA COMPLETA (Ciclo por Ciclo) ---
            print("\n========================================================")
            print(f"TABLA DE CRECIMIENTO: {model_id}")
            print("========================================================")
            print(final_models.to_string())
            print("\n")
            
            # --- CÓDIGO DE GUARDADO (Se mantiene para guardar los datos brutos) ---
            csv_file_name = f"{model_id}_biomasa.csv"
            csv_output_path = os.path.join(OUTPUT_CSV_FOLDER, csv_file_name)
            final_models.to_csv(csv_output_path, index=False)
            
            print(f"ÉXITO: {model_id} simulado. Serie de Tiempo guardada en {csv_file_name}")

        else:
            print(f"ADVERTENCIA (Inviable): Modelo {model_id} falló la simulación Batch (resultado = None).")

    except Exception as e:
        print(f"ERROR CRÍTICO: Falló el procesamiento de {model_id}: {e}. Archivo: {file_name}")


    finally:
        # --- BLOQUE FINALLY ---
        if final_models is not None:
            # Si el modelo fue viable, el finally no necesita imprimir la tabla de nuevo
            pass 
        else:
            # Imprime el mensaje de advertencia si falló la simulación
            print(f"--- Iteración {model_id} finalizada. Estado: FALLO DE SIMULACIÓN/NO REGISTRADO ---")


# --- IMPRESIÓN DEL RESUMEN FINAL (Se elimina el bloque de tabla de resumen) ---
# Solo imprimimos el total de modelos procesados
print(f"\nTotal de modelos cargados: {len(all_models)}")