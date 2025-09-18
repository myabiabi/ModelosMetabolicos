#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


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
ST164_2 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml'))
ST164_2.id = 'ST00164'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164_2.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164_2)


test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
#test_tube.set_specific_metabolite("prbamp_e", 10)
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
output_path = os.path.join(output_folder, 'ST00164_2.png')
plt.savefig(output_path)

###################################
ST164_3_model = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml')

ST164_3 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml'))
ST164_3.id = 'ST00164'


# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164_3.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164_3)

test_tube.set_specific_metabolite("prbamp_e", 10)

test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
#test_tube.set_specific_metabolite("prbamp_e", 10)
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
test_tube.set_specific_metabolite("cbl1_e", 0.01)


sim_params = c.params()
experiment = c.comets(test_tube, sim_params)
experiment.run()

ax = experiment.total_biomass.plot(x = 'cycle', color = 'orange')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas_/CARVEME'
output_path = os.path.join(output_folder, 'ST00164_3.png')
plt.savefig(output_path)
##
# Lista de posibles metabolitos traza extracelulares
trace_metabolites = [
    "ca2_e", "cl_e", "cobalt2_e", "cu2_e", "fe2_e", "fe3_e", "k_e", "mg2_e", 
    "mn2_e", "na1_e", "nh4_e", "ni2_e", "so4_e", "pi_e", "zn2_e", "h_e", "o2_e", "h2o_e"
]

# Filtrar cuáles de esos están en el modelo
present = [m for m in trace_metabolites if m in [met.id for met in ST164_2.metabolites]]

print("Metabolitos traza presentes en el modelo:")
for m in present:
    print("-", m)

# Lista de metabolitos traza
trace_metabolites = [
    "ca2_e", "cl_e", "cobalt2_e", "cu2_e", "fe2_e", "fe3_e", "k_e", "mg2_e", 
    "mn2_e", "na1_e", "nh4_e", "ni2_e", "so4_e", "pi_e", "zn2_e", "h_e", "o2_e", "h2o_e"
]


ST164_gem = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml')

# Asegúrate de que ST164_2 sea un modelo COBRA válido
present = [m for m in trace_metabolites if m in [met.id for met in ST164_gem.metabolites]]

print("Metabolitos traza presentes en el modelo:")
for m in present:
    print("-", m)


# =================
# 080725
# =================

ST164_model = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml')
ST164_model.medium

medio_modelo  = [
    'EX_14glucan_e', 'EX_23camp_e', 'EX_23ccmp_e', 'EX_23cgmp_e', 'EX_23cump_e',
    'EX_23dhbzs3_e', 'EX_25dkglcn_e', 'EX_2ameph_e', 'EX_2hxmp_e', 'EX_2m35mdntha_e',
    'EX_2pg_e', 'EX_2pglyc_e', 'EX_35dnta_e', 'EX_3amp_e', 'EX_3cmp_e',
    'EX_3pg_e', 'EX_3ump_e', 'EX_4abut_e', 'EX_4ahmmp_e', 'EX_4hba_e',
    'EX_5dglcn_e', 'EX_Lcyst_e', 'EX_abt__L_e', 'EX_ac_e', 'EX_acac_e',
    'EX_acald_e', 'EX_acgam_e', 'EX_acmana_e', 'EX_acnam_e', 'EX_actn__R_e',
    'EX_akg_e', 'EX_ala_B_e', 'EX_ala_L_asp__L_e', 'EX_ala_L_glu__L_e', 'EX_ala_L_thr__L_e',
    'EX_ala__D_e', 'EX_ala__L_e', 'EX_ala_gln_e', 'EX_ala_his_e', 'EX_ala_leu_e',
    'EX_alagly_e', 'EX_alahis_e', 'EX_alaleu_e', 'EX_alathr_e', 'EX_alatrp_e',
    'EX_amp_e', 'EX_arbt_e', 'EX_arg__L_e', 'EX_asn__L_e', 'EX_aso3_e',
    'EX_aso4_e', 'EX_asp__D_e', 'EX_asp__L_e', 'EX_bhb_e', 'EX_btn_e',
    'EX_but_e', 'EX_buts_e', 'EX_bz_e', 'EX_ca2_e', 'EX_cd2_e',
    'EX_cell4_e', 'EX_cellb_e', 'EX_cgly_e', 'EX_chol_e', 'EX_cit_e',
    'EX_cl_e', 'EX_cmcbtt_e', 'EX_cmp_e', 'EX_co2_e', 'EX_co_e',
    'EX_cobalt2_e', 'EX_cu2_e', 'EX_cys__L_e', 'EX_cytd_e', 'EX_dad_2_e',
    'EX_damp_e', 'EX_dcmp_e', 'EX_dcyt_e', 'EX_dextrin_e', 'EX_dgsn_e',
    'EX_din_e', 'EX_drib_e', 'EX_dtmp_e', 'EX_dump_e', 'EX_duri_e',
    'EX_eths_e', 'EX_etoh_e', 'EX_fcmcbtt_e', 'EX_fe2_e', 'EX_fe3_e',
    'EX_fe3dcit_e', 'EX_fe3pyovd_kt_e', 'EX_fol_e', 'EX_for_e', 'EX_fru_e',
    'EX_fum_e', 'EX_g3pc_e', 'EX_g3pg_e', 'EX_g3pi_e', 'EX_g3ps_e',
    'EX_gal_bD_e', 'EX_galman4_e', 'EX_galman6_e', 'EX_galt_e', 'EX_galur_e',
    'EX_gam_e', 'EX_glc__D_e', 'EX_glc__aD_e', 'EX_glcman4_e', 'EX_glcman6_e',
    'EX_glcn__D_e', 'EX_glcn_e', 'EX_glcur_e', 'EX_gln__L_e', 'EX_glu__L_e',
    'EX_glutar_e', 'EX_gly_asn__L_e', 'EX_gly_asp__L_e', 'EX_gly_cys_e', 'EX_gly_e',
    'EX_gly_gln_e', 'EX_gly_glu__L_e', 'EX_gly_leu_e', 'EX_gly_met_e', 'EX_gly_phe_e',
    'EX_gly_pro__L_e', 'EX_gly_tyr_e', 'EX_glyald_e', 'EX_glyb_e', 'EX_glyc3p_e',
    'EX_glyc_e', 'EX_glyclt_e', 'EX_glygln_e', 'EX_glyglu_e', 'EX_glygly_e',
    'EX_glyglygln_e', 'EX_glymet_e', 'EX_glyphe_e', 'EX_glyser_e', 'EX_gmp_e',
    'EX_gthox_e', 'EX_gthrd_e', 'EX_gua_e', 'EX_h2_e', 'EX_h2o2_e',
    'EX_h2o_e', 'EX_h2s_e', 'EX_h_e', 'EX_ham_e', 'EX_hco3_e',
    'EX_hexs_e', 'EX_his__L_e', 'EX_hisgly_e', 'EX_hishis_e', 'EX_hqn_e',
    'EX_hxa_e', 'EX_hxan_e', 'EX_ile__L_e', 'EX_imp_e', 'EX_inost_e',
    'EX_ins_e', 'EX_istfrnA_e', 'EX_istfrnB_e', 'EX_istnt_e', 'EX_k_e',
    'EX_lac__D_e', 'EX_lac__L_e', 'EX_leu__L_e', 'EX_leuleu_e', 'EX_lipoate_e',
    'EX_lys__L_e', 'EX_lysglugly_e', 'EX_mal__L_e', 'EX_malt_e', 'EX_malthx_e',
    'EX_malttr_e', 'EX_man_e', 'EX_meoh_e', 'EX_met_L_ala__L_e', 'EX_met__D_e',
    'EX_met__L_e', 'EX_metox__R_e', 'EX_metox_e', 'EX_metsox_R__L_e', 'EX_metsox_S__L_e',
    'EX_mg2_e', 'EX_mn2_e', 'EX_mnl_e', 'EX_mobd_e', 'EX_mso3_e',
    'EX_n2_e', 'EX_na1_e', 'EX_nac_e', 'EX_nh4_e', 'EX_ni2_e',
    'EX_no2_e', 'EX_no3_e', 'EX_o2_e', 'EX_orn__L_e', 'EX_orn_e',
    'EX_oxa_e', 'EX_pea_e', 'EX_pep_e', 'EX_phe__L_e', 'EX_pheme_e',
    'EX_pi_e', 'EX_pime_e', 'EX_pnto__R_e', 'EX_ppi_e', 'EX_pro__L_e',
    'EX_progly_e', 'EX_prohisglu_e', 'EX_ptrc_e', 'EX_pyovd_kt_e', 'EX_rib__D_e',
    'EX_ribflv_e', 'EX_s_e', 'EX_salcn_e', 'EX_ser__D_e', 'EX_ser__L_e',
    'EX_serglugly_e', 'EX_so3_e', 'EX_so4_e', 'EX_spmd_e', 'EX_stfrnA_e',
    'EX_stfrnB_e', 'EX_succ_e', 'EX_sucr_e', 'EX_sula_e', 'EX_taur_e',
    'EX_thm_e', 'EX_thr__L_e', 'EX_thymd_e', 'EX_tnt_e', 'EX_tre_e',
    'EX_trp__L_e', 'EX_tsul_e', 'EX_tyr__L_e', 'EX_udcpdp_e', 'EX_udcpp_e',
    'EX_ump_e', 'EX_ura_e', 'EX_urea_e', 'EX_uri_e', 'EX_val__L_e',
    'EX_xan_e', 'EX_xyl__D_e', 'EX_zn2_e'
]


from cobra import Reaction

#test_tube.set_specific_metabolite("prbamp_e", 10)

# Crear una reacción de intercambio para b12_e
ex_prbamp = Reaction('EX_prbamp_e')
ex_prbamp.name = 'Exchange for phosphoridocil'
ex_prbamp.lower_bound = -1000.  # permite importarlo
ex_prbamp.upper_bound = 1000.   # permite exportarlo
ex_prbamp.add_metabolites({ST164_model.metabolites.get_by_id('prbamp_e'): -1})

ST164_model.add_reactions([ex_prbamp])

################
from cobra import Reaction
from cobra import Metabolite


# 1. Crear el metabolito extracellular
prbamp_e = Metabolite(
    id='prbamp_e',
    name='Phosphoribosyl-AMP',
    compartment='e',
    formula='C10H15N5O10P2',  # Fórmula química, puedes ajustar si conoces otra
    charge=-2
)

# 2. Agregar el metabolito al modelo
ST164_model.add_metabolites([prbamp_e])
ST42.add_metabolites([prbamp_e])


# 3. Crear la reacción de intercambio (exchange reaction)
ex_prbamp = Reaction('EX_prbamp_e')
ex_prbamp.name = 'Exchange for phosphoribosyl-AMP'
ex_prbamp.lower_bound = -1000.0  # entrada al modelo (import)
ex_prbamp.upper_bound = 1000.0   # salida del modelo (export)

# 4. Asociar el metabolito a la reacción
ex_prbamp.add_metabolites({prbamp_e: -1})

# 5. Agregar la reacción al modelo
ST164_model.add_reactions([ex_prbamp])

ST164_model = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/ST00164.xml'))

test_tube.set_specific_metabolite("prbamp_e", 10)



################################################

from cobra import Metabolite, Reaction
from cobra import Metabolite, Reaction

# Buscar metabolito o agregarlo si no existe
prbamp_e = next((m for m in ST164_model.metabolites if m.id == "prbamp_e"), None)
if prbamp_e is None:
    prbamp_e = Metabolite(
        id='prbamp_e',
        name='Phosphoribosyl-AMP',
        compartment='e',
        formula='C10H15N5O10P2',
        charge=-2
    )
    ST164_model.add_metabolites([prbamp_e])

# Verificar/agregar la reacción de intercambio
ex_id = "EX_prbamp_e"
ex_prbamp = next((r for r in ST164_model.reactions if r.id == ex_id), None)
if ex_prbamp is None:
    ex_prbamp = Reaction(ex_id)
    ex_prbamp.name = "Exchange reaction for prbamp_e"
    ex_prbamp.lower_bound = -1000.0
    ex_prbamp.upper_bound = 1000.0
    ex_prbamp.add_metabolites({prbamp_e: -1})
    ST164_model.add_reactions([ex_prbamp])

# Añadir modelo y metabolito al test tube
test_tube.add_model(ST164_model)
test_tube.set_specific_metabolite("prbamp_e", 10)

# =================
#  090325 
# =================

ST00164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/carve164.xml')
ST164_dimon = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00164_diamon.xml')

print(len(ST00164.exchanges))
print(len(ST164_dimon.exchanges))


ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00164_diamon.xml'))


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

output_folder = 'graficas/CARVEME/DIMONT'
output_path = os.path.join(output_folder, 'ST000164_diamont.png')
plt.savefig(output_path)

# =================
#  090925
# =================
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

ST164_d = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/ST00164_diamon.xml'))
ST164_d.id = 'Bacillus'
# set its initial biomass, 5e-6 gr at coordinate [0,0]
ST164_d.initial_pop = [0, 0, 5e-8]

# create an empty layout
test_tube = c.layout()

# add the models to the test tube
test_tube.add_model(ST164_d)


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

ax = experiment.total_biomass.plot(x = 'cycle', color = 'green')
ax.set_ylabel("Biomass (gr.)")

output_folder = 'graficas/CARVEME/DIMONT'
output_path = os.path.join(output_folder, '164.png')
plt.savefig(output_path)

# =================
#  160925
# =================
#usando el GEM con gapfiling de carveme _NW

#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/new_ST00164.xml'))
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
output_path = os.path.join(output_folder, 'ST00164_new_.png')
plt.savefig(output_path)

#ahora usando el GEM de gapseq 
#Start by loading required packages, including the COMETS toolbox
import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os


ST164 = c.model(cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/gapseq_models/bac60.xml'))
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

output_folder = 'graficas_/GapSeq'
output_path = os.path.join(output_folder, 'ST00042_.png')
plt.savefig(output_path)


# ==============
# 091725
# ================

import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os

#ST00164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve164.xml')
#ST00164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00164_diamon.xml')
ST00164 = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00164dd.xml')
ST164 = c.model(ST00164)

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

ax = experiment.total_biomass.plot(x = 'cycle', color = 'green')
ax.set_ylabel("Biomass (gr.)")
output_folder = '03_graficas/CARVEME/DIAMONT_2'
output_path = os.path.join(output_folder, 'ST00164.png')
plt.savefig(output_path)
