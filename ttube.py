import cobra
import cobra.io
import cometspy as c

#cobra.io.load_model('textbook')
# Load a textbook example model using the COBRAPy toolbox 
test_model = cobra.io.load_model('textbook')
# Use the above model to create a COMETS model
test_model = c.model(test_model)

# Change comets specific parameters, e.g. the initial biomass of the model
# Notre 
test_model.initial_pop = [0, 0, 1e-7] 


# Create a parameters object with default values 
my_params = c.params()

# Change the value of a parameter, for example number of simulation cycles
my_params.set_param('maxCycles', 100)

# Set some writeTotalBiomassLog parameter to True, in order to save the output
my_params.set_param('writeTotalBiomassLog', True)

# See avaliable parameters and their values
my_params.show_params()

my_layout = c.layout(test_model)
my_layout.media

my_simulation = c.comets(my_layout, my_params)
my_simulation.run()
print(my_simulation.run_output)
print(my_simulation.run_errors)

import cometspy as c
import cobra.io
import matplotlib.pyplot as plt

# Create empty 1x1 layout
test_tube = c.layout()

# Add 11mM glucose and remove o2
test_tube.set_specific_metabolite('glc__D_e', 0.011)
test_tube.set_specific_metabolite('o2_e', 0)

# Add the rest of nutrients unlimited (ammonia, phosphate, water and protons)
test_tube.set_specific_metabolite('nh4_e',1000);
test_tube.set_specific_metabolite('pi_e',1000);
test_tube.set_specific_metabolite('h2o_e',1000);
test_tube.set_specific_metabolite('h_e',1000);

####################3

# create the model using CobraPy functionality
e_coli_cobra = cobra.io.load_model('textbook')


# use the loaded model to build a comets model
e_coli = c.model(e_coli_cobra)

# remove the bounds from glucose import (will be set dynamically by COMETS)
e_coli.change_bounds('EX_glc__D_e', -1000, 1000)

# set the model's initial biomass
e_coli.initial_pop = [0, 0, 5e-6]

# add it to the test_tube
test_tube.add_model(e_coli)

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

#############################
import os
import matplotlib.pyplot as plt

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
output_path = os.path.join(output_folder, 'concentraciones.png')
plt.savefig(output_path)

# Mostrar figura
plt.show()


##pruebaaas


