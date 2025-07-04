import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt


RC3 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'))
RC3.id = 'rc3'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
RC3.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()
test_tube.add_model(RC3)

lb_10_metabolites = {
    "h2o_e": 100,
    "o2_e": 10,
    "pi_e": 10,
    "amp_e": 10,
    "glu__L_e": 10,
    "pheme_e": 0.1,
    "mg2_e": 0.1,
    "gly_e": 0.1,
    "zn2_e": 10,
    "ala__L_e": 0.1,
    "lys__L_e": 0.1,
    "asp__L_e": 0.1,
    "cmp_e": 0.1,
    "so4_e": 0.1,
    "arg__L_e": 0.1,
    "ser__L_e": 0.1,
    "cu2_e": 0.1,
    "met__L_e": 0.1,
    "ca2_e": 0.1,
    "trp__L_e": 0.1,
    "phe__L_e": 0.1,
    "h_e": 0.1,
    "tyr__L_e": 0.1,
    "cys__L_e": 0.1,
    "ump_e": 0.1,
    "ura_e": 0.1,
    "cl_e": 0.1,
    "leu__L_e": 0.1,
    "his__L_e": 0.1,
    "gmp_e": 0.1,
    "pro__L_e": 0.1,
    "cobalt2_e": 10,
    "val__L_e": 0.1,
    "thr__L_e": 0.1,
    "adn_e": 0.01,
    "thymd_e": 0.01,
    "k_e": 10,
    "pydx_e": 10,
    "nac_e": 10,
    "pphn_e": 10,
    "ribflv_e": 10,
    "hxan_e": 10,
    "h2s_e": 0.01,
    "ins_e": 0.01,
    "uri_e": 0.01,
    "gsn_e": 0.01,
    "ile__L_e": 0.1,
    "skm_e": 0.01,
    "fol_e": 0.01,
    "dadn_e": 0.01,
    "hg2_e": 10,
    "lipoate_e": 0.01,
    "pnto__R_e": 0.01,
    "dcyt_e": 0.01,
    "thmmp_e": 0.01,
    "na1_e": 10,
    "cd2_e": 10,
    "aso4_e": 10,
    "glc__D_e": 0.01,
    "fe2_e": 10,
    "fe3_e": 10,
    "cro4_e": 10
}


# Add medium metabolites to the layout
for met, conc in lb_10_metabolites.items():
    test_tube.set_specific_metabolite(met, conc)

static_mets = ['h2o_e', 'o2_e', 'na1_e', 'cl_e', 'k_e']
for met in static_mets:
    test_tube.set_specific_static(met, lb_10_metabolites[met])


comp_params = c.params()
comp_params.set_param('maxCycles', 240)


comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()
#####################


#import matplotlib.pyplot as plt

# Copiamos el DataFrame para no modificar el original
#biomass = comp_assay.total_biomass.copy()

# Calculamos el tiempo en horas
#biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

# Definimos explícitamente las columnas que queremos graficar (tus bacterias)
#bacteria_ids = ['rc3']

# Hacemos la gráfica: tiempo en x, biomasa de cada bacteria en y
#ax = biomass.plot(x='t', y=bacteria_ids, marker='o', linestyle='-')

#ax.set_xlabel("Tiempo (horas)")
#ax.set_ylabel("Biomasa (gr)")
#ax.set_title("Crecimiento RC3 (LB 10%)")
#ax.legend(title='Cepas')

#plt.show()
import os 
biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/competition_assay/C2R_RC3'
output_path = os.path.join(output_folder, '0704_RC3.png')
plt.savefig(output_path)
