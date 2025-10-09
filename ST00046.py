#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

#ST164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00164.xml')
#ST60 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00060.xml')
ST46 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00046.xml')



ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml'))
ST164.id = 'ST00164'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164)


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
test_tube.set_specific_metabolite("nh3_c_e", 10)
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

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'orange')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas_/CARVEME'
output_path = os.path.join(output_folder, 'ST00164_.png')
plt.savefig(output_path)


####################################################################################


ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml'))
ST164.id = 'ST00164'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164)


test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
#test_tube.set_specific_metabolite("prbamp_e", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("mn2_e", 10)
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
#test_tube.set_specific_metabolite("adn_e", 0.01)
test_tube.set_specific_metabolite("thymd_e", 0.01)
test_tube.set_specific_metabolite("k_e", 10)
test_tube.set_specific_metabolite("h2s_e", 0.01)
test_tube.set_specific_metabolite("ins_e", 0.01)
test_tube.set_specific_metabolite("uri_e", 0.01)
test_tube.set_specific_metabolite("mg2_e", 10)
#test_tube.set_specific_metabolite("gsn_e", 0.01)
test_tube.set_specific_metabolite("ile__L_e", 0.1)
test_tube.set_specific_metabolite("cys__L_e", 0.1)
#test_tube.set_specific_metabolite("skm_e", 0.01)
test_tube.set_specific_metabolite("fol_e", 0.01)
#test_tube.set_specific_metabolite("dadn_e", 0.01)
test_tube.set_specific_metabolite("lipoate_e", 0.01)
test_tube.set_specific_metabolite("na1_e", 10)
test_tube.set_specific_metabolite("cd2_e", 10)
test_tube.set_specific_metabolite("aso4_e", 10)
test_tube.set_specific_metabolite("fe2_e", 10)
test_tube.set_specific_metabolite("fe3_e", 10)
#test_tube.set_specific_metabolite("cro4_e", 10)
#test_tube.set_specific_metabolite("nh3_c_e", 10)
test_tube.set_specific_metabolite("pheme_e", 10)
test_tube.set_specific_metabolite("cmp_e", 10)
test_tube.set_specific_metabolite("ump_e", 10)
test_tube.set_specific_metabolite("gmp_e", 10)
#test_tube.set_specific_metabolite("pydx_e", 10)
test_tube.set_specific_metabolite("nac_e", 10)
test_tube.set_specific_metabolite("ribflv_e", 10)
#test_tube.set_specific_metabolite("pphn_e", 10)
test_tube.set_specific_metabolite("hxan_e", 10)
#test_tube.set_specific_metabolite("thmpp_e", 0.01)
#test_tube.set_specific_metabolite("cbl1_e", 0.01)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'orange')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas_/CARVEME'
output_path = os.path.join(output_folder, 'ST00164_.png')
plt.savefig(output_path)


#090325
#Ensayo con parametro de dimont (alineador) cambiado

import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

ST00046 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00046.xml')
ST00046_diamon = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00046_diamon.xml')

print(len(ST00046.exchanges))
print(len(ST00046_diamon.exchanges))
ST46 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00046_diamon.xml'))


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST46.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST46)

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
test_tube.set_specific_metabolite("nh3_c_e", 10)
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

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'orange')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/CARVEME/DIMONT'
output_path = os.path.join(output_folder, 'ST00046_dimont.png')
plt.savefig(output_path)


# 090925

import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

ST00046 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/DEFAULT/carve46.xml')
ST00046_diamon = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00046_diamon.xml')
ST00046_egg = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/eggnote/ST46_egg.xml')
ST00046_egg_2 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/eggnote/ST46fna.xml')
print(len(ST00046.exchanges))
print(len(ST00046_diamon.exchanges))
print(len(ST00046_egg.exchanges))
print(len(ST00046_egg_2.exchanges))


ST46_egg = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/eggnote/ST46fna.xml'))
ST46_egg.id = 'Bacillus'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST46_egg.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST46_egg)

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
test_tube.set_specific_metabolite("nh3_c_e", 10)
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

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'pink')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/CARVEME/EGG'
output_path = os.path.join(output_folder, 'ST00046.png')
plt.savefig(output_path)

# ==================
# 160925
# ===================
#usando el GEM de gapseq

import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

C2R = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM_1/Gapseq/gps_ST00046.xml'))
C2R.id = 'ST001'

C2R.initial_pop = [0, 0, 5e-8]

test_tube = c.layout()
test_tube.add_model(C2R)
test_tube.set_specific_metabolite("h2o_e", 100, static = False)
test_tube.set_specific_metabolite("o2_e", 10, static = False)
test_tube.set_specific_metabolite("pi_e", 10, static = False)
test_tube.set_specific_metabolite("prbamp_e", 10, static = False)
test_tube.set_specific_metabolite("glu__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("mg2_e", 0.1, static = False)
test_tube.set_specific_metabolite("gly_e", 0.1, static = False)
test_tube.set_specific_metabolite("zn2_e", 10, static = False)
test_tube.set_specific_metabolite("ala__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("lys__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("asp__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("so4_e", 0.1, static = False)
test_tube.set_specific_metabolite("arg__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("ser__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("cu2_e", 0.1, static = False)
test_tube.set_specific_metabolite("met__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("trp__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("phe__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("h_e", 0.1, static = False)
test_tube.set_specific_metabolite("tyr__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("cys__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("ura_e", 0.1, static = False)
test_tube.set_specific_metabolite("cl_e", 0.1, static = False)
test_tube.set_specific_metabolite("leu__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("his__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("pro__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("cobalt2_e", 10, static = False)
test_tube.set_specific_metabolite("val__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("thr__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("adn_e", 0.01, static = False)
test_tube.set_specific_metabolite("thymd_e", 0.01, static = False)
test_tube.set_specific_metabolite("k_e", 10, static = False)
test_tube.set_specific_metabolite("h2s_e", 0.01, static = False)
test_tube.set_specific_metabolite("ins_e", 0.01, static = False)
test_tube.set_specific_metabolite("uri_e", 0.01, static = False)
test_tube.set_specific_metabolite("mg2_e", 10, static = False)
test_tube.set_specific_metabolite("gsn_e", 0.01, static = False)
test_tube.set_specific_metabolite("ile__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("cys__L_e", 0.1, static = False)
test_tube.set_specific_metabolite("skm_e", 0.01, static = False)
test_tube.set_specific_metabolite("fol_e", 0.01, static = False)
test_tube.set_specific_metabolite("dadn_e", 0.01, static = False)
test_tube.set_specific_metabolite("lipoate_e", 0.01, static = False)
test_tube.set_specific_metabolite("na1_e", 10, static = False)
test_tube.set_specific_metabolite("cd2_e", 10, static = False)
test_tube.set_specific_metabolite("aso4_e", 10, static = False)
test_tube.set_specific_metabolite("fe2_e", 10, static = False)
test_tube.set_specific_metabolite("fe3_e", 10, static = False)
test_tube.set_specific_metabolite("cro4_e", 10, static = False)
test_tube.set_specific_metabolite("nh3_e", 10, static = False)
test_tube.set_specific_metabolite("pheme_e", 10, static = False)
test_tube.set_specific_metabolite("cmp_e", 10, static = False)
test_tube.set_specific_metabolite("ump_e", 10, static = False)
test_tube.set_specific_metabolite("gmp_e", 10, static = False)
test_tube.set_specific_metabolite("pydx_e", 10, static = False)
test_tube.set_specific_metabolite("nac_e", 10, static = False)
test_tube.set_specific_metabolite("ribflv_e", 10, static = False)
test_tube.set_specific_metabolite("pphn_e", 10, static = False)
test_tube.set_specific_metabolite("hxan_e", 10, static = False)

comp_params = c.params()
comp_params.set_param('maxCycles', 240)


comp_assay = c.comets(test_tube, comp_params)
comp_assay.run()

ax = comp_assay.total_biomass.plot(x = 'cycle')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas'
output_path = os.path.join(output_folder, '080425_4.png')
plt.savefig(output_path)

# ===============
# 091725
# ====================
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

#ST00046 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve46.xml')
#ST00046 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00046_diamon.xml')
ST00046 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00046dd.xml')
ST46 = c.model(ST00046)
ST46.id = 'ST00046'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST46.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST46)

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
test_tube.set_specific_metabolite("nh3_c_e", 10)
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
# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']
for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)
    
sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'red')
ax.set_ylabel("Biomass (gr.)")
output_folder = '03_graficas/CARVEME/DIAMONT_2'
output_path = os.path.join(output_folder, 'ST00046.png')
plt.savefig(output_path)

#100625

#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

#ST164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00164.xml')
#ST60 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00060.xml')
ST46 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00046.xml')



ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_gapseq/gem_clust/ST00046.xml'))
ST164.id = 'ST00164'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164)


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
test_tube.set_specific_metabolite("nh3_c_e", 10)
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

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'orange')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'Documents/practicas/MODELOS/03_graficas/GapSeq'
output_path = os.path.join(output_folder, 'ST00164_.png')
plt.savefig(output_path)

