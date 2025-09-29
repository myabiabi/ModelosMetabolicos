import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

ST00143 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00143dd.xml')
ST143 = c.model(ST00143)
ST143.id = "Paenibacillus"
ST00042 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00042_diamon.xml')
ST42 = c.model(ST00042)
ST42.id = "Pseudomonas"
ST00164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00164_diamon.xml')
ST164 = c.model(ST00164)
ST164.id = "Bacillus"

ST143.initial_pop = [0, 0, 5e-8]
ST42.initial_pop = [0, 0, 5e-8]
ST164.initial_pop = [0, 0, 5e-8]

test_tube = c.layout()
test_tube.add_model(ST143)
test_tube.add_model(ST42)
test_tube.add_model(ST164)

test_tube.set_specific_metabolite('glc__D_e', 0.10)

trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i,1000)
    test_tube.set_specific_static(i,1000)


comp_params = c.params()
comp_params.set_param('maxCycles', 240)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()
############
biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

# Graficar con colores y líneas más gruesas
myplot = biomass.drop(columns=['cycle']).plot(
    x='t',
    color=['yellow', 'purple', 'green'],  # colores para cada bacteria
    linewidth=2                     # grosor de las líneas
)

myplot.set_ylabel("Biomass (gr.)")

# Guardar la figura
output_folder = '03_graficas/'
os.makedirs(output_folder, exist_ok=True)  # crea la carpeta si no existe
output_path = os.path.join(output_folder, "AHhahah.png")  # agrega extensión
plt.savefig(output_path, dpi=300)
plt.show()

print(biomass.columns)
print(biomass)