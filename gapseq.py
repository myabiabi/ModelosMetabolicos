import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import cobra.io

all_models = {} 
test_tube = c.layout()
sim_params = c.params()


path_list = glob.glob('01_data/models_gapseq/gem_clust/ST00*.xml')

for model_path in path_list:
    if "-draft.xml" in model_path:
                continue
    try:                        
        model_id = os.path.basename(model_path).replace('.xml', '') 
        cobra_models = cobra.io.read_sbml_model(model_path)
        processed_models = c.model(cobra_models) 
        all_models[model_id] = processed_models
        print(f"Modelo {model_id} cargado y procesado exitosamente.")  
    except Exception as e:
        print(f"Error al procesar el modelo {model_id}: {e}. Archivo: {model_path}")

print(f"Total de modelos cargados: {len(all_models)}")
for model_id in all_models.items():
      model_id.initial_pop = [0, 0, 1e-8]
      test_tube.add_model(model_id)
      test_tube.set_specific_metabolite("h2o_e", 100)
      test_tube.set_specific_metabolite("o2_e", 10)
      test_tube.set_specific_metabolite("pi_e", 10)
      test_tube.set_specific_metabolite("prbamp_e", 10)
      test_tube.set_specific_metabolite("glu__L_e", 0.1)
      test_tube.set_specific_metabolite("mn2_e", 10)
      test_tube.set_specific_metabolite("gly_e", 0.1)
      test_tube.set_specific_metabolite("zn2_e", 10)
      test_tube.set_specific_metabolite("ala__L_e", 0.1)
      test_tube.set_specific_metabolite("lys__L_e", 0.1)
      test_tube.set_specific_metabolite("asp__L_e", 0.1)
      test_tube.set_specific_metabolite("so4_e", 0.1)
      test_tube.set_specific_metabolite("arg__L_e", 0.1)
      test_tube.set_specific_metabolite("ser__L_e", 0.1)
      test_tube.set_specific_metabolite("cu2_e", 0.1)
      test_tube.set_specific_metabolite("met__L_e", 0.1)
      test_tube.set_specific_metabolite("trp__L_e", 0.1)
      test_tube.set_specific_metabolite("phe__L_e", 0.1)
      test_tube.set_specific_metabolite("h_e", 0.1)
      test_tube.set_specific_metabolite("tyr__L_e", 0.1)
      test_tube.set_specific_metabolite("cys__L_e", 0.1)
      test_tube.set_specific_metabolite("ura_e", 0.1)
      test_tube.set_specific_metabolite("cl_e", 0.1)
      test_tube.set_specific_metabolite("leu__L_e", 0.1) 
      test_tube.set_specific_metabolite("his__L_e", 0.1)
      test_tube.set_specific_metabolite("pro__L_e", 0.1)
      test_tube.set_specific_metabolite("cobalt2_e", 10)
      test_tube.set_specific_metabolite("val__L_e", 0.1)
      test_tube.set_specific_metabolite("thr__L_e", 0.1)
      test_tube.set_specific_metabolite("adn_e", 0.01)
      test_tube.set_specific_metabolite("thymd_e", 0.01)
      test_tube.set_specific_metabolite("k_e", 10)
      test_tube.set_specific_metabolite("h2s_e", 0.01)
      test_tube.set_specific_metabolite("ins_e", 0.01)
      test_tube.set_specific_metabolite("uri_e", 0.01)
      test_tube.set_specific_metabolite("mg2_e", 10)
      test_tube.set_specific_metabolite("gsn_e", 0.01)
      test_tube.set_specific_metabolite("ile__L_e", 0.1)
      test_tube.set_specific_metabolite("cys__L_e", 0.1)
      test_tube.set_specific_metabolite("skm_e", 0.01)
      test_tube.set_specific_metabolite("fol_e", 0.01)
      test_tube.set_specific_metabolite("dadn_e", 0.01)
      test_tube.set_specific_metabolite("lipoate_e", 0.01)
      test_tube.set_specific_metabolite("na1_e", 10)
      test_tube.set_specific_metabolite("cd2_e", 10)
      test_tube.set_specific_metabolite("aso4_e", 10)
      test_tube.set_specific_metabolite("fe2_e", 10)
      test_tube.set_specific_metabolite("fe3_e", 10)
      test_tube.set_specific_metabolite("cro4_e", 10)
      test_tube.set_specific_metabolite("nh3_c_e", 10)
      test_tube.set_specific_metabolite("pheme_e", 10)
      test_tube.set_specific_metabolite("cmp_e", 10)
      test_tube.set_specific_metabolite("ump_e", 10)
      test_tube.set_specific_metabolite("gmp_e", 10)
      test_tube.set_specific_metabolite("pydx_e", 10)
      test_tube.set_specific_metabolite("nac_e", 10)
      test_tube.set_specific_metabolite("ribflv_e", 10)
      test_tube.set_specific_metabolite("pphn_e", 10)
      test_tube.set_specific_metabolite("hxan_e", 10)
      test_tube.set_specific_metabolite("thmpp_e", 0.01)
      test_tube.set_specific_metabolite("cbl1_e", 0.01)
      trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                        'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']
for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)
    
    experiment = c.comets(test_tube, sim_params)
    experiment.run()    
    results_df = experiment.total_biomass
