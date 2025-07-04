import cometspy as c
import cobra.io
import matplotlib.pyplot as plt

#############
test_tube = c.layout()
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("gly_e", 0.1)
test_tube.set_specific_metabolite("zn2_e", 10)
test_tube.set_specific_metabolite("ala__L_e", 0.1)
test_tube.set_specific_metabolite("lys_L_e", 0.1)
test_tube.set_specific_metabolite("asp_L_e", 0.1)

# create the model using CobraPy functionality
ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'
RC3_cobra = cobra.io.read_sbml_model(ruta_RC3)

# use the loaded model to build a comets model
RC3 = c.model(RC3_cobra)

# remove the bounds from glucose import (will be set dynamically by COMETS)
RC3.change_bounds('EX_glc__D_e', -1000, 1000)

# set the model's initial biomass
RC3.initial_pop = [0, 0, 5e-6]

# add it to the test_tube
test_tube.add_model(RC3)

# Set the parameters that are different from the default
sim_params = c.params()
sim_params.set_param('defaultVmax', 18.5)
sim_params.set_param('defaultKm', 0.000015)
sim_params.set_param('maxCycles', 1000)
sim_params.set_param('timeStep', 0.01)
sim_params.set_param('spaceWidth', 1)
sim_params.set_param('maxSpaceBiomass', 10)
sim_params.set_param('minSpaceBiomass', 1e-11)
sim_params.set_param('writeMediaLog', True)

experiment = c.comets(test_tube, sim_params)
experiment.run()

#############
import os

# Crear la carpeta si no existe
output_folder = 'graficas'
os.makedirs(output_folder, exist_ok=True)

ax = experiment.total_biomass.plot(x = 'cycle')
ax.set_ylabel("Biomass (gr.)")

media = experiment.media.copy()
media = media[media.conc_mmol<900]

fig, ax = plt.subplots()
media.groupby('metabolite').plot(x='cycle', ax =ax, y='conc_mmol')
ax.legend(('acetate','ethanol', 'formate', 'glucose'))
ax.set_ylabel("Concentration (mmol)")

# Guardar figura en la carpeta
output_path = os.path.join(output_folder, '063025_TTEST_RC3_nutrientes_LB.png')
plt.savefig(output_path)

# Mostrar figura
plt.show()


##pruebaaas



