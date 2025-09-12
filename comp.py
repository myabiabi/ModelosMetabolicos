
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

ST42 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DIMONT_2/ST00042dd.xml')
ST60 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DIMONT_2/ST00060dd.xml')
ST109 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DIMONT_2/ST00109dd.xml')
ST143 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DIMONT_2/ST00143dd.xml')
ST164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DIMONT_2/ST00164dd.xml')


len(ST42.reactions)
len(ST60.reactions)
len(ST109.reactions)
len(ST143.reactions)
len(ST164.reactions)

ST60.exchanges


ST42.id ='Pseudomonas'
ST143.id ='Paenibacillus'
ST164.id ='Bacillus'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST42.initial_pop = [0, 0, 5e-8]
ST143.initial_pop = [0, 0, 5e-8]
ST164.initial_pop = [0, 0, 5e-8]



# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST42)
test_tube.add_model(ST143)
test_tube.add_model(ST164)


# Define main metabolites
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
test_tube.set_specific_metabolite("prbamp_e", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("mn2_e", 10)
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
test_tube.set_specific_metabolite("leu__L_e", 0.1) 
test_tube.set_specific_metabolite("his__L_e", 0.1)
test_tube.set_specific_metabolite("pro__L_e", 0.1)
test_tube.set_specific_metabolite("val__L_e", 0.1)
test_tube.set_specific_metabolite("thr__L_e", 0.1)
test_tube.set_specific_metabolite("adn_e", 0.01)
test_tube.set_specific_metabolite("thymd_e", 0.01)
test_tube.set_specific_metabolite("h2s_e", 0.01)
test_tube.set_specific_metabolite("ins_e", 0.01)
test_tube.set_specific_metabolite("uri_e", 0.01)
test_tube.set_specific_metabolite("gsn_e", 0.01)
test_tube.set_specific_metabolite("ile__L_e", 0.1)
test_tube.set_specific_metabolite("skm_e", 0.01)
test_tube.set_specific_metabolite("fol_e", 0.01)
test_tube.set_specific_metabolite("dadn_e", 0.01)
test_tube.set_specific_metabolite("lipoate_e", 0.01)
test_tube.set_specific_metabolite("cd2_e", 10)
test_tube.set_specific_metabolite("aso4_e", 10)
test_tube.set_specific_metabolite("fe2_e", 10)
test_tube.set_specific_metabolite("fe3_e", 10)
test_tube.set_specific_metabolite("cro4_e", 10)
test_tube.set_specific_metabolite("pheme_e", 10)
test_tube.set_specific_metabolite("cmp_e", 10)
test_tube.set_specific_metabolite("ump_e", 10)
test_tube.set_specific_metabolite("gmp_e", 10)
test_tube.set_specific_metabolite("pydx_e", 10)
test_tube.set_specific_metabolite("nac_e", 10)
test_tube.set_specific_metabolite("ribflv_e", 10)
test_tube.set_specific_metabolite("pphn_e", 10)
test_tube.set_specific_metabolite("hxan_e", 10)
test_tube.set_specific_metabolite("thmpp_e", 0.01)
test_tube.set_specific_metabolite("cbl1_e", 0.01)

# Add typical trace metabolites and oxygen as static
trace_metabolites = [
    'ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e',
    'h_e', 'k_e', 'h2o_e', 'mg2_e', 'mn2_e', 'mobd_e',
    'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e'
]

for met in trace_metabolites:
    test_tube.set_specific_metabolite(met, 1000)
    test_tube.set_specific_static(met, 1000)

comp_params = c.params()
comp_params.set_param('maxCycles', 240)

comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

#print(comp_assay.run_output)

#Exception in thread "Thread-0" java.lang.ArrayIndexOutOfBoundsException: Index 396 out of bounds for length 228