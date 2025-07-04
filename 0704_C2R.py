import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt

C2R = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_C2R.xml'))
C2R.id = 'c2r'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
C2R.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()
test_tube.add_model(C2R)

lb_10_metabolites = {
    'ala__L_e': 0.1,
    'arg__L_e': 0.1,
    'asn__L_e': 0.1,
    'asp__L_e': 0.1,
    'cys__L_e': 0.1,
    'gln__L_e': 0.1,
    'glu__L_e': 0.1,
    'gly_e': 0.1,
    'his__L_e': 0.1,
    'ile__L_e': 0.1,
    'leu__L_e': 0.1,
    'lys__L_e': 0.1,
    'met__L_e': 0.1,
    'phe__L_e': 0.1,
    'pro__L_e': 0.1,
    'ser__L_e': 0.1,
    'thr__L_e': 0.1,
    'trp__L_e': 0.1,
    'tyr__L_e': 0.1,
    'val__L_e': 0.1,
    'ade_e': 0.01,
    'ura_e': 0.01,
    'gmp_e': 0.01,
    'h2o_e': 1000,
    'pi_e': 10,
    'so4_e': 10,
    'nh4_e': 10,
    'na1_e': 1000,
    'cl_e': 1000,
    'k_e': 1000,
    'o2_e': 1000
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

#import matplotlib.pyplot as plt

# Copiamos el DataFrame para no modificar el original
#biomass = comp_assay.total_biomass.copy()

# Calculamos el tiempo en horas
#biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

# Definimos explícitamente las columnas que queremos graficar (tus bacterias)
#bacteria_ids = ['c2r']

# Hacemos la gráfica: tiempo en x, biomasa de cada bacteria en y
#ax = biomass.plot(x='t', y=bacteria_ids, marker='o', linestyle='-')

##ax.set_xlabel("Tiempo (horas)")
#ax.set_ylabel("Biomasa (gr)")
#ax.set_title("Crecimiento de C2R (LB 10%)")
#ax.legend(title='C2R')

#plt.show()
import os
biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/competition_assay/C2R_RC3'
output_path = os.path.join(output_folder, '0704_C2R.png')
plt.savefig(output_path)

