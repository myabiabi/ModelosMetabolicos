import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np # Necesario para plt.cm.get_cmap

all_models = {} 
test_tube = c.layout()
sim_params = c.params()
output_folder = '03_graficas/GapSeq/gem_clust/individual_biomass' # Carpeta final

# --- 1. CICLO DE CARGA Y FILTRADO (LLENA all_models y test_tube) ---
path_list = glob.glob('01_data/models_gapseq/gem_clust/ST00*.xml')

for model_path in path_list:
    if "-draft.xml" in model_path:
                continue
    try:                        
        model_id = os.path.basename(model_path).replace('.xml', '') 
        cobra_models = cobra.io.read_sbml_model(model_path)
        processed_models = c.model(cobra_models) 
        all_models[model_id] = processed_models
        
        # --- CONFIGURACIÓN CRÍTICA DENTRO DEL BUCLE (CORREGIDO) ---
        # El bucle debe iterar sobre all_models.items() para acceder a los objetos
        # PERO: Simplificamos el código aquí. Ya que 'processed_models' es el objeto
        # actual, lo usamos directamente y luego lo añadimos.
        processed_models.initial_pop = [0, 0, 1e-8]
        test_tube.add_model(processed_models)
        # ----------------------------------------------------------
        
        print(f"Modelo {model_id} cargado y añadido.")
    except Exception as e:
        print(f"Error al procesar el modelo {model_id}: {e}. Archivo: {model_path}")

print(f"\nTotal de modelos cargados y añadidos a test_tube: {len(all_models)}")


# --- 2. CONFIGURACIÓN DEL MEDIO AMBIENTE (FUERA DEL BUCLE) ---

print("Configurando el medio ambiente...")

# A. Metales traza y configuración estática (CORREGIDO)
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                        'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']
for met_id in trace_metabolites:
    test_tube.set_specific_metabolite(met_id, 1000)
    test_tube.set_specific_static(met_id, 1000)

# B. Metabolitos específicos (Usamos el diccionario que tenías, asumiendo que es completo)
metabolites_to_set = {
    "o2_e": 10, "pi_e": 10, "prbamp_e": 10, "glu__L_e": 0.1, "mn2_e": 10, "gly_e": 0.1, 
    "zn2_e": 10, "ala__L_e": 0.1, "lys__L_e": 0.1, "asp__L_e": 0.1, "so4_e": 0.1, "arg__L_e": 0.1, 
    "ser__L_e": 0.1, "cu2_e": 0.1, "met__L_e": 0.1, "trp__L_e": 0.1, "phe__L_e": 0.1, "h_e": 0.1, 
    "tyr__L_e": 0.1, "cys__L_e": 0.1, "ura_e": 0.1, "cl_e": 0.1, "leu__L_e": 0.1, "his__L_e": 0.1, 
    "pro__L_e": 0.1, "cobalt2_e": 10, "val__L_e": 0.1, "thr__L_e": 0.1, "adn_e": 0.01, 
    "thymd_e": 0.01, "k_e": 10, "h2s_e": 0.01, "ins_e": 0.01, "uri_e": 0.01, "mg2_e": 10, 
    "gsn_e": 0.01, "ile__L_e": 0.1, "skm_e": 0.01, "fol_e": 0.01, "dadn_e": 0.01, 
    "lipoate_e": 0.01, "na1_e": 10, "cd2_e": 10, "aso4_e": 10, "fe2_e": 10, "fe3_e": 10, 
    "cro4_e": 10, "nh3_c_e": 10, "pheme_e": 10, "cmp_e": 10, "ump_e": 10, "gmp_e": 10, 
    "pydx_e": 10, "nac_e": 10, "ribflv_e": 10, "pphn_e": 10, "hxan_e": 10, "thmpp_e": 0.01, 
    "cbl1_e": 0.01
}
for met_id, conc in metabolites_to_set.items():
     test_tube.set_specific_metabolite(met_id, conc)


# --- 3. EJECUCIÓN DE LA SIMULACIÓN (¡UNA SOLA VEZ!) ---
print("\n===== Creando y Ejecutando la Simulación COMETS =====")
experiment = c.comets(test_tube, sim_params)
experiment.run()
results_df = experiment.biomass


# --- 4. CICLO DE GRAFICACIÓN INDIVIDUAL ---

# Preparar la carpeta de salida
os.makedirs(output_folder, exist_ok=True) 
model_ids_in_results = results_df['model'].unique()
num_models_in_results = len(model_ids_in_results)
colors = plt.cm.get_cmap('viridis', num_models_in_results) 

print(f"\nGuardando {num_models_in_results} gráficas individuales en {output_folder}...")

for i, model_id in enumerate(model_ids_in_results):
    
    cepa_data = results_df[results_df['model'] == model_id]
    
    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    
    # Graficar y asignar color único
    cepa_data.plot(x='cycle', y='biomass', ax=ax, label=model_id, color=colors(i), linewidth=2)

    # Configuración de los ejes
    ax.set_title(f"Biomasa a lo largo del tiempo para {model_id}")
    ax.set_ylabel("Biomass (gr.)")
    ax.set_xlabel("Ciclo de Simulación")
    
    # Construcción dinámica del nombre del archivo
    file_name = f"{model_id}_Biomass.png"
    output_path = os.path.join(output_folder, file_name)
    
    plt.legend().set_visible(False) # Ocultar la leyenda si solo se grafica 1
    plt.savefig(output_path)
    plt.close() 
    
    print(f"Gráfico guardado: {file_name}")

print("\nGuardado de gráficas individuales completado.")
