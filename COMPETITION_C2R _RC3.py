#COMPETITION ASAY C2R y RC3
#############COMPETITION ASAY

# Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt

# load the models and perform the mutation

##cobra.io.load_model('textbook')
#test_model = cobra.test.create_test_model('textbook')


# Definir la ruta del archivo de modelo
ruta_C2R = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_C2R.xml'

# Cargar el modelo usando COBRApy y COMETS
C2R = c.model(cobra.io.read_sbml_model(ruta_C2R))  # Usar la ruta correcta del archivo
C2R.id = 'c2r'

ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'
RC3 = c.model(cobra.io.read_sbml_model(ruta_RC3))  # Lo mismo aquí
RC3.id = 'rc3'

# Configurar la población inicial en ambas condiciones
C2R.initial_pop = [0, 0, 5e-8]  # Biomasa inicial en las coordenadas [0, 0]
RC3.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(C2R)
test_tube.add_model(RC3)

# Add glucose to the media 
test_tube.set_specific_metabolite('glc__D_e', 0.01)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)


comp_params = c.params()
comp_params.set_param('maxCycles', 240)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']


myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

# Guardar figura en la carpeta
output_folder = 'graficas'
output_path = os.path.join(output_folder, 'C2RyRC3_2.png')
plt.savefig(output_path)


#We can quantitatively analyze the results. For example, we can compute the competitive fitness of the mutant respect to the wild-type as the ratio of the biomass increase of the mutant divided by that of the wild-type:
cfit = (biomass.loc[biomass['t'] == 24, 'rc3'].iloc[0]/biomass.loc[biomass['t'] == 0, 'rc3'].iloc[0])/(biomass.loc[biomass['t'] == 24, 'c2r'].iloc[0]/biomass.loc[biomass['t'] == 0, 'c2r'].iloc[0])
cfit
print(cfit)

#Simulating serial transfers
serial_params = c.params()
serial_params.set_param('maxCycles', 150) 
#en el ejemplo usan "240*25" para los cilos, simular 4 transferencias en serie de 24h cada una
#esa cantidad de ciclos no corre 
#25*2 si
#50*2 si 
serial_params.set_param('batchDilution', True)
serial_params.set_param('dilFactor', 0.01)
serial_params.set_param('dilTime', 24)

serial_expt = c.comets(test_tube,serial_params)
serial_expt.JAVA_CLASSPATH = comp_assay.JAVA_CLASSPATH
serial_expt.run()

biomass = serial_expt.total_biomass
biomass['transfer'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

myplot = biomass.drop(columns=['cycle']).plot(x = 'transfer')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas'
output_path = os.path.join(output_folder, 'C2RyRC3_2.png')
plt.savefig(output_path)

##
