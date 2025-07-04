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


#


