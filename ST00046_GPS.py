
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