#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


RC3 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_ST00154.xml'))
RC3.id = 'ST00154'

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
test_tube.set_specific_metabolite("nh3_c", 10)
test_tube.set_specific_metabolite("pheme", 10)
test_tube.set_specific_metabolite("cmp", 10)
test_tube.set_specific_metabolite("ump", 10)
test_tube.set_specific_metabolite("gmp", 10)
test_tube.set_specific_metabolite("pydx", 10)
test_tube.set_specific_metabolite("nac", 10)
test_tube.set_specific_metabolite("ribflv", 10)
test_tube.set_specific_metabolite("pphn", 10)
test_tube.set_specific_metabolite("hxan", 10)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 500)

comp_params = c.params()
comp_params.set_param('maxCycles', 500)
comp_params.set_param('timeStep', 1)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

###########

biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/competition_assay'
output_path = os.path.join(output_folder, '0721_ST00154_CVM.png')
plt.savefig(output_path)



