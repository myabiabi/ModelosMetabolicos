import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


#ruta_C2R = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_C2R.xml'
ecoli_model = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml')
ecoli = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml'))
ecoli.id = 'ecoli'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
ecoli.initial_pop = [0, 0, 5e-8]


# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ecoli)
 
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

biomass = comp_assay.total_biomass
biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']/24

myplot = biomass.drop(columns=['cycle']).plot(x = 't')
myplot.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/ecoli'
output_path = os.path.join(output_folder, 'ecoli.png')
plt.savefig(output_path)

########################################################################ENSAYO DE COMPETENCIA DOCUMENTACIÓN 
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


wt = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml'))
wt.id = 'wt'
mut = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml'))
mut.change_bounds('TPI', 0,0)
mut.id = 'TPI_KO'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
wt.initial_pop = [0, 0, 5e-8]
mut.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube0 = c.layout()

# add the models to the test tube
test_tube0.add_model(wt)
test_tube0.add_model(mut)


# Add glucose to the media 
test_tube0.set_specific_metabolite('glc__D_e', 0.01)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites0 = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites0:
    test_tube0.set_specific_metabolite(i, 1000)
    test_tube0.set_specific_static(i, 1000)


comp_params0 = c.params()
comp_params0.set_param('maxCycles', 240)

comp_assay0 = c.comets(test_tube0, comp_params0)
comp_assay0.run()

biomass0 = comp_assay0.total_biomass
biomass0['t'] = biomass0['cycle'] * comp_assay0.parameters.all_params['timeStep']

myplot0 = biomass0.drop(columns=['cycle']).plot(x = 't')
myplot0.set_ylabel("Biomass (gr.)")

output_folder = 'graficas'
output_path = os.path.join(output_folder, 'ecoli1.png')
plt.savefig(output_path)



##################################################SOLO CRECE LA E. COLI WT

import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


wt1 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml'))
wt1.id = 'wt'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
wt1.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(wt1)


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

output_folder = 'graficas'
output_path = os.path.join(output_folder, 'ecoli_wt1.png')
plt.savefig(output_path)


###############################################################E. COLI CRECE CON NUTRIENTES DIFERENTES 
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


wt2 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/e_coli_core.xml'))
wt2.id = 'wt'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
wt2.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube2 = c.layout()

# add the models to the test tube
test_tube2.add_model(wt2)


# Add glucose to the media 
test_tube2.set_specific_metabolite('glc__D_e', 0.01)
test_tube2.set_specific_metabolite("h2o_e", 100)
test_tube2.set_specific_metabolite("o2_e", 10)
test_tube2.set_specific_metabolite("pi_e", 10)
test_tube2.set_specific_metabolite("prbamp_e", 10)
test_tube2.set_specific_metabolite("glu__L_e", 0.1)
test_tube2.set_specific_metabolite("mn2_e", 10)
test_tube2.set_specific_metabolite("gly_e", 0.1)
test_tube2.set_specific_metabolite("zn2_e", 10)
test_tube2.set_specific_metabolite("ala__L_e", 0.1)
test_tube2.set_specific_metabolite("lys__L_e", 0.1)
test_tube2.set_specific_metabolite("asp__L_e", 0.1)
test_tube2.set_specific_metabolite("so4_e", 0.1)
test_tube2.set_specific_metabolite("arg__L_e", 0.1)
test_tube2.set_specific_metabolite("ser__L_e", 0.1)
test_tube2.set_specific_metabolite("cu2_e", 0.1)
test_tube2.set_specific_metabolite("met__L_e", 0.1)
test_tube2.set_specific_metabolite("trp__L_e", 0.1)
test_tube2.set_specific_metabolite("phe__L_e", 0.1)
test_tube2.set_specific_metabolite("h_e", 0.1)
test_tube2.set_specific_metabolite("tyr__L_e", 0.1)
test_tube2.set_specific_metabolite("cys__L_e", 0.1)
test_tube2.set_specific_metabolite("ura_e", 0.1)
test_tube2.set_specific_metabolite("cl_e", 0.1)
test_tube2.set_specific_metabolite("leu__L_e", 0.1) 
test_tube2.set_specific_metabolite("his__L_e", 0.1)
test_tube2.set_specific_metabolite("pro__L_e", 0.1)
test_tube2.set_specific_metabolite("cobalt2_e", 10)
test_tube2.set_specific_metabolite("val__L_e", 0.1)
test_tube2.set_specific_metabolite("thr__L_e", 0.1)
test_tube2.set_specific_metabolite("adn_e", 0.01)
test_tube2.set_specific_metabolite("thymd_e", 0.01)
test_tube2.set_specific_metabolite("k_e", 10)
test_tube2.set_specific_metabolite("h2s_e", 0.01)
test_tube2.set_specific_metabolite("ins_e", 0.01)
test_tube2.set_specific_metabolite("uri_e", 0.01)
test_tube2.set_specific_metabolite("mg2_e", 10)
test_tube2.set_specific_metabolite("gsn_e", 0.01)
test_tube2.set_specific_metabolite("ile__L_e", 0.1)
test_tube2.set_specific_metabolite("cys__L_e", 0.1)
test_tube2.set_specific_metabolite("skm_e", 0.01)
test_tube2.set_specific_metabolite("fol_e", 0.01)
test_tube2.set_specific_metabolite("dadn_e", 0.01)
test_tube2.set_specific_metabolite("lipoate_e", 0.01)
test_tube2.set_specific_metabolite("na1_e", 10)
test_tube2.set_specific_metabolite("cd2_e", 10)
test_tube2.set_specific_metabolite("aso4_e", 10)
test_tube2.set_specific_metabolite("fe2_e", 10)
test_tube2.set_specific_metabolite("fe3_e", 10)
test_tube2.set_specific_metabolite("cro4_e", 10)
test_tube2.set_specific_metabolite("nh3_c_e", 10)
test_tube2.set_specific_metabolite("pheme_e", 10)
test_tube2.set_specific_metabolite("cmp_e", 10)
test_tube2.set_specific_metabolite("ump_e", 10)
test_tube2.set_specific_metabolite("gmp_e", 10)
test_tube2.set_specific_metabolite("pydx_e", 10)
test_tube2.set_specific_metabolite("nac_e", 10)
test_tube2.set_specific_metabolite("ribflv_e", 10)
test_tube2.set_specific_metabolite("pphn_e", 10)
test_tube2.set_specific_metabolite("hxan_e", 10)
test_tube2.set_specific_metabolite("thmpp_e", 0.01)
test_tube2.set_specific_metabolite("cbl1_e", 0.01)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites2 = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites2:
    test_tube2.set_specific_metabolite(i, 1000)
    test_tube2.set_specific_static(i, 1000)


comp_params2 = c.params()
comp_params2.set_param('maxCycles', 240)

comp_assay2 = c.comets(test_tube2, comp_params2)
comp_assay2.run()

biomass2 = comp_assay2.total_biomass
biomass2['t'] = biomass2['cycle'] * comp_assay2.parameters.all_params['timeStep']

myplot2 = biomass2.drop(columns=['cycle']).plot(x = 't')
myplot2.set_ylabel("Biomass (gr.)")

output_folder2 = 'graficas'
output_path2 = os.path.join(output_folder2, 'ecoli_wt4.png')
plt.savefig(output_path2)


#si le quito: test_tube2.set_specific_metabolite('glc__D_e', 0.01) no crece nada, el la gráfica ecoli_wt3.png, 
#si le agrego el resto de metabolitos, pero conservio ('glc__D_e', 0.01), crece igual que si solo tuviera la glc_D 