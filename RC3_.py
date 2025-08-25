##########################JULIO 01###########################
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


#ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'


RC3 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'))
RC3.id = 'RC3'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
RC3.initial_pop = [0, 0, 5e-8]


# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(RC3)


test_tube.set_specific_metabolite("h2o", 100)
test_tube.set_specific_metabolite("o2", 10)
test_tube.set_specific_metabolite("pi", 10)
test_tube.set_specific_metabolite("amp", 10)
test_tube.set_specific_metabolite("glu__L_e", 10)
test_tube.set_specific_metabolite("pheme", 0.1)
test_tube.set_specific_metabolite("mg2", 0.1)
test_tube.set_specific_metabolite("gly", 0.1)
test_tube.set_specific_metabolite("zn2", 10)
test_tube.set_specific_metabolite("ala__L", 0.1)
test_tube.set_specific_metabolite("lys_L", 0.1)
#Warning: The added metabolite (lys_L_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("asp_L", 0.1)
#Warning: The added metabolite (asp_L_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("cmp", 0.1)
test_tube.set_specific_metabolite("so4", 0.1)
test_tube.set_specific_metabolite("arg__L", 0.1)
test_tube.set_specific_metabolite("ser__L", 0.1)
test_tube.set_specific_metabolite("cu2", 0.1)
test_tube.set_specific_metabolite("met__L", 0.1)
test_tube.set_specific_metabolite("met__L", 0.1)
test_tube.set_specific_metabolite("ca2", 0.1)
test_tube.set_specific_metabolite("trp__L", 0.1)
test_tube.set_specific_metabolite("phe__L", 0.1)
test_tube.set_specific_metabolite("h", 0.1)
test_tube.set_specific_metabolite("tyr__L", 0.1)
test_tube.set_specific_metabolite("cys__L", 0.1)
test_tube.set_specific_metabolite("ump", 0.1)
test_tube.set_specific_metabolite("ura", 0.1)
test_tube.set_specific_metabolite("cl", 0.1)
test_tube.set_specific_metabolite("leu__L", 0.1) 
test_tube.set_specific_metabolite("his__L", 0.1)
test_tube.set_specific_metabolite("gmp", 0.1)
test_tube.set_specific_metabolite("pro__L", 0.1)
test_tube.set_specific_metabolite("cobalt2", 10)
test_tube.set_specific_metabolite("val__L", 0.1)
test_tube.set_specific_metabolite("thr__L", 0.1)
test_tube.set_specific_metabolite("adn", 0.01)
#Warning: The added metabolite (adn_p) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("thymd", 0.01)
test_tube.set_specific_metabolite("k", 10)
test_tube.set_specific_metabolite("pydx", 10)
test_tube.set_specific_metabolite("nac", 10)
test_tube.set_specific_metabolite("pphn", 10)
test_tube.set_specific_metabolite("ribflv", 10)
test_tube.set_specific_metabolite("hxan", 10)
test_tube.set_specific_metabolite("h2s", 0.01)
test_tube.set_specific_metabolite("ins", 0.01)
test_tube.set_specific_metabolite("uri", 0.01)
test_tube.set_specific_metabolite("mg2", 10)
test_tube.set_specific_metabolite("gsn", 0.01)
#Warning: The added metabolite (gsn_c) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("ile__L", 0.1)
test_tube.set_specific_metabolite("cys__L", 0.1)
test_tube.set_specific_metabolite("skm", 0.01)
#Warning: The added metabolite (skm_c) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("fol", 0.01)
test_tube.set_specific_metabolite("dadn", 0.01)
test_tube.set_specific_metabolite("hg2", 10)
#Warning: The added metabolite (dadn_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("lipoate", 0.01)
test_tube.set_specific_metabolite("pnto__R", 0.01)
test_tube.set_specific_metabolite("dcyt", 0.01)
test_tube.set_specific_metabolite("thmmp", 0.01)
test_tube.set_specific_metabolite("na1", 10)
test_tube.set_specific_metabolite("cd2", 10)
test_tube.set_specific_metabolite("aso4", 10)
test_tube.set_specific_metabolite("glc__D", 0.01)
test_tube.set_specific_metabolite("fe2", 10)
test_tube.set_specific_metabolite("fe3", 10)
test_tube.set_specific_metabolite("cro4", 10)
#Warning: The added metabolite (cro4_p) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("nh3", 10)
#Warning: The added metabolite (cro4_p) is not able to be taken up by any of the current models






# Add typical trace metabolites and oxygen coli as static
#trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     #'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

#for i in trace_metabolites:
    ###test_tube.set_specific_metabolite(i, 1000)
    #test_tube.set_specific_static(i, 1000)

comp_params = c.params()
comp_params.set_param('maxCycles', 240)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

###########
biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas'
output_path = os.path.join(output_folder, 'RC3_070325_4.png')
plt.savefig(output_path)


#######################JULIO 04#####################
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



###################################JULIO 01########################
# Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


#ruta_C2R = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_C2R.xml'

RC3 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'))
RC3.id = 'rc3'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
RC3.initial_pop = [0, 0, 5e-8]


# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(RC3)
 
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
test_tube.set_specific_metabolite("prbamp_e", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("mg2_e", 0.1)
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
test_tube.set_specific_metabolite("nh3_e", 10)


#Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

comp_params = c.params()
comp_params.set_param('maxCycles', 240)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

###########
biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/competition_assay/C2R_RC3'
output_path = os.path.join(output_folder, '0704_RC3_4.png')
plt.savefig(output_path)

