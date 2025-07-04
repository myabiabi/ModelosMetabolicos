# Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


ruta_C2R = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_C2R.xml'
ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'


C2R = c.model(cobra.io.read_sbml_model(ruta_C2R))
C2R.id = 'c2r'
RC3 = c.model(cobra.io.read_sbml_model(ruta_RC3))
RC3.id = 'rc3'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
C2R.initial_pop = [0, 0, 5e-8]
RC3.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(C2R)
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

#biomass = comp_assay.total_biomass
#biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

#myplot = biomass.drop(columns=['cycle']).plot(x = 't')
#myplot.set_ylabel("Biomass (gr.)")


###########
#biomass = comp_assay.total_biomass
#biomass['transfer'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

#myplot = biomass.drop(columns=['cycle']).plot(x = 'transfer')
#myplot.set_ylabel("Biomass (gr.)")

##output_folder = 'graficas/competition_assay/C2R_RC3'
#output_path = os.path.join(output_folder, '063025_C2R_RC3_competencia_3.png')
#plt.savefig(output_path)

#plt.show
##


# Guardar figura en la carpeta
#output_folder = 'graficas/competition_assay/C2R_RC3'
#output_path = os.path.join(output_folder, '0704_C2R_RC3_biomass.png')
#plt.savefig(output_path)


#We can quantitatively analyze the results. For example, we can compute the competitive fitness of the mutant respect to the wild-type as the ratio of the biomass increase of the mutant divided by that of the wild-type:
#cfit = (biomass.loc[biomass['t'] == 24, 'c2r'].iloc[0]/biomass.loc[biomass['t'] == 0, 'c2r'].iloc[0])/(biomass.loc[biomass['t'] == 24, 'rc3'].iloc[0]/biomass.loc[biomass['t'] == 0, 'rc3'].iloc[0])
#cfit
#print(cfit)

#Simulating serial transfers
#serial_params = c.params()
#serial_params.set_param('maxCycles', 150) 
#en el ejemplo usan "240*25" para los cilos, simular 4 transferencias en serie de 24h cada una
#esa cantidad de ciclos no corre 
#25*2 si
#50*2 si 
#serial_params.set_param('batchDilution', True)
#serial_params.set_param('dilFactor', 0.01)
#serial_params.set_param('dilTime', 24)

#serial_expt = c.comets(test_tube,serial_params)
#serial_expt.JAVA_CLASSPATH = comp_assay.JAVA_CLASSPATH
#serial_expt.run()

#biomass = serial_expt.total_biomass
#biomass['transfer'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

#myplot = biomass.drop(columns=['cycle']).plot(x = 'transfer')
#myplot.set_ylabel("Biomass (gr.)")

#output_folder = 'graficas/competition_assay/C2R_RC3'
#output_path = os.path.join(output_folder, '0704_C2R_RC3_transfer.png')
#plt.savefig(output_path)

#plt.show 

biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/competition_assay/C2R_RC3'
output_path = os.path.join(output_folder, '0704_C2R_RC3_competencia_LB_1.png')
plt.savefig(output_path)
