import cometspy as c
import cobra
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

YR343_R2A=cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00042.xml')
GM17_R2A=cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00046.xml')
AP49_R2A=cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/carveme_models/LB/new_ST00060.xml')


#Remove bounds from exchange reactions
for i in YR343_R2A.reactions:
    if 'EX_' in i.id:
        i.lower_bound=-1000.0

for i in GM17_R2A.reactions:
    if 'EX_' in i.id:
        i.lower_bound=-1000.0

for i in AP49_R2A.reactions:
    if 'EX_' in i.id:
        i.lower_bound=-1000.0


YR343=c.model(YR343_R2A)
GM17=c.model(GM17_R2A)
AP49=c.model(AP49_R2A)

#Open exchange reations so that extracellular metabolite concentrations and Michaelis-Menten kinetics control uptake bounds
YR343.open_exchanges()
GM17.open_exchanges()
AP49.open_exchanges()


YR343.obj_style="MAX_OBJECTIVE_MIN_TOTAL" #default FBA option is "MAXIMIZE_OBJECTIVE_FLUX"
GM17.obj_style="MAX_OBJECTIVE_MIN_TOTAL"
AP49.obj_style="MAX_OBJECTIVE_MIN_TOTAL"


#YR343
YR343.change_bounds('EX_cpd00027_e0',-0.1741,1000) #####Glucose 

YR343.change_bounds('EX_cpd00001_e0',-1000,1000) #H2O
YR343.change_bounds('EX_cpd00007_e0',-1000,1000) #O2
YR343.change_bounds('EX_cpd00009_e0',-1000,1000) #Phosphate
YR343.change_bounds('EX_cpd00013_e0',-1000,1000) #NH3

YR343.change_bounds('EX_cpd00018_e0',-1000,1000) #AMP

YR343.change_bounds('EX_cpd00020_e0',-1000,1000) #Pyruvate

YR343.change_bounds('EX_cpd00023_e0',-0.1741,1000) #####Glutamate

YR343.change_bounds('EX_cpd00028_e0',-1000,1000) # #Heme

YR343.change_bounds('EX_cpd00030_e0',-1000,1000) #Mn2+

YR343.change_bounds('EX_cpd00033_e0',-0.1741,1000) #####Glycine

YR343.change_bounds('EX_cpd00034_e0',-1000,1000) #Zn2+

YR343.change_bounds('EX_cpd00035_e0',-0.1741,1000) #####Alanine
YR343.change_bounds('EX_cpd00039_e0',-0.1741,1000) #####Lysine
YR343.change_bounds('EX_cpd00041_e0',-0.1741,1000) #####Aspartate

YR343.change_bounds('EX_cpd00046_e0',-1000,1000) #CMP

YR343.change_bounds('EX_cpd00048_e0',-1000,1000) #Sulfate

YR343.change_bounds('EX_cpd00051_e0',-0.1741,1000) #####Arginine

YR343.change_bounds('EX_cpd00053_e0',-0.1741,1000) #####Glutamine

YR343.change_bounds('EX_cpd00054_e0',-0.1741,1000) #####Serine

YR343.change_bounds('EX_cpd00058_e0',-1000,1000) #Cu2+

YR343.change_bounds('EX_cpd00060_e0',-0.1741,1000) #####Methionine

YR343.change_bounds('EX_cpd00063_e0',-1000,1000) #Ca2+

YR343.change_bounds('EX_cpd00065_e0',-0.1741,1000) #####Tryptophan
YR343.change_bounds('EX_cpd00066_e0',-0.1741,1000) #####Phenylalanine

YR343.change_bounds('EX_cpd00067_e0',-1000,1000) #H+

YR343.change_bounds('EX_cpd00069_e0',-0.1741,1000) #####Tyrosine

YR343.change_bounds('EX_cpd00084_e0',-0.1741,1000) #####Cysteine

YR343.change_bounds('EX_cpd00091_e0',-1000,1000) #UMP

YR343.change_bounds('EX_cpd00092_e0',-1000,1000) #Uracil

YR343.change_bounds('EX_cpd00099_e0',-1000,1000) #Cl-

YR343.change_bounds('EX_cpd00107_e0',-0.1741,1000) #####Leucine
YR343.change_bounds('EX_cpd00119_e0',-0.1741,1000) #####Histidine

YR343.change_bounds('EX_cpd00126_e0',-1000,1000) #GMP

YR343.change_bounds('EX_cpd00129_e0',-0.1741,1000) #####Proline

YR343.change_bounds('EX_cpd00132_e0',-0.1741,1000) #####Asparagine

YR343.change_bounds('EX_cpd00149_e0',-1000,1000) #Co2+

YR343.change_bounds('EX_cpd00156_e0',-0.1741,1000) #####Valine
YR343.change_bounds('EX_cpd00161_e0',-0.1741,1000) #####Threonine

YR343.change_bounds('EX_cpd00182_e0',-1000,1000) #Adenosine
YR343.change_bounds('EX_cpd00184_e0',-1000,1000) #Thymidine

YR343.change_bounds('EX_cpd00205_e0',-1000,1000) #K+

YR343.change_bounds('EX_cpd00215_e0',-1000,1000) #Pyridoxal
YR343.change_bounds('EX_cpd00218_e0',-1000,1000) #Niacin
YR343.change_bounds('EX_cpd00220_e0',-1000,1000) #Riboflavin
YR343.change_bounds('EX_cpd00226_e0',-1000,1000) #HYXN Hypoxanthine

YR343.change_bounds('EX_cpd00239_e0',-1000,1000) #H2S

YR343.change_bounds('EX_cpd00244_e0',-1000,1000) #Ni2+

YR343.change_bounds('EX_cpd00246_e0',-1000,1000) #Inosine
YR343.change_bounds('EX_cpd00249_e0',-1000,1000) #Uridine

YR343.change_bounds('EX_cpd00254_e0',-1000,1000) #Mg

YR343.change_bounds('EX_cpd00311_e0',-1000,1000) #Guanosine

YR343.change_bounds('EX_cpd00322_e0',-0.1741,1000) #####Isoleucine
YR343.change_bounds('EX_cpd00381_e0',-0.1741,1000) #####Cystine

YR343.change_bounds('EX_cpd00393_e0',-1000,1000) #Folate

YR343.change_bounds('EX_cpd00438_e0',-1000,1000) #Deoxyadenosine

YR343.change_bounds('EX_cpd00531_e0',-1000,1000) #Hg2+

YR343.change_bounds('EX_cpd00541_e0',-1000,1000) #Lipoate

YR343.change_bounds('EX_cpd00644_e0',-1000,1000) #PAN Pantothenate
YR343.change_bounds('EX_cpd00654_e0',-1000,1000) #Deoxycytidine
YR343.change_bounds('EX_cpd00793_e0',-1000,1000) #Thiamine phosphate

YR343.change_bounds('EX_cpd00971_e0',-1000,1000) #Na+
YR343.change_bounds('EX_cpd01012_e0',-1000,1000) #Cd2+

YR343.change_bounds('EX_cpd01048_e0',-1000,1000) #Arsenate

YR343.change_bounds('EX_cpd03424_e0',-1000,1000) #Vitamin B12

YR343.change_bounds('EX_cpd10515_e0',-1000,1000) #Fe2+
YR343.change_bounds('EX_cpd10516_e0',-1000,1000) #Fe3+

YR343.change_bounds('EX_cpd11574_e0',-1000,1000) #Molybdate
YR343.change_bounds('EX_cpd11595_e0',-1000,1000) #chromate
YR343.change_bounds('EX_cpd11657_e0',-1000,1000) #Starch



#GM17
GM17.change_bounds('EX_cpd00027_e0',-10,1000) #Glucose

GM17.change_bounds('EX_cpd00001_e0',-1000,1000) #H2O
GM17.change_bounds('EX_cpd00007_e0',-1000,1000) #O2
GM17.change_bounds('EX_cpd00009_e0',-1000,1000) #Phosphate
GM17.change_bounds('EX_cpd00013_e0',-1000,1000) #NH3

GM17.change_bounds('EX_cpd00018_e0',-1000,1000) #AMP

GM17.change_bounds('EX_cpd00020_e0',-1000,1000) #Pyruvate

GM17.change_bounds('EX_cpd00023_e0',-10,1000) #Glutamate

GM17.change_bounds('EX_cpd00028_e0',-1000,1000) # #Heme

GM17.change_bounds('EX_cpd00030_e0',-1000,1000) #Mn2+

GM17.change_bounds('EX_cpd00033_e0',-10,1000) #Glycine

GM17.change_bounds('EX_cpd00034_e0',-1000,1000) #Zn2+

GM17.change_bounds('EX_cpd00035_e0',-10,1000) #Alanine
GM17.change_bounds('EX_cpd00039_e0',-10,1000) #Lysine
GM17.change_bounds('EX_cpd00041_e0',-10,1000) #Aspartate

GM17.change_bounds('EX_cpd00046_e0',-1000,1000) #CMP

GM17.change_bounds('EX_cpd00048_e0',-1000,1000) #Sulfate

GM17.change_bounds('EX_cpd00051_e0',-10,1000) #Arginine

GM17.change_bounds('EX_cpd00053_e0',-10,1000) #Glutamine

GM17.change_bounds('EX_cpd00054_e0',-10,1000) #Serine

GM17.change_bounds('EX_cpd00058_e0',-1000,1000) #Cu2+

GM17.change_bounds('EX_cpd00060_e0',-10,1000) #Methionine

GM17.change_bounds('EX_cpd00063_e0',-1000,1000) #Ca2+

GM17.change_bounds('EX_cpd00065_e0',-10,1000) #Tryptophan
GM17.change_bounds('EX_cpd00066_e0',-10,1000) #Phenylalanine

GM17.change_bounds('EX_cpd00067_e0',-1000,1000) #H+

GM17.change_bounds('EX_cpd00069_e0',-10,1000) #Tyrosine

GM17.change_bounds('EX_cpd00084_e0',-10,1000) #Cysteine

GM17.change_bounds('EX_cpd00091_e0',-1000,1000) #UMP

GM17.change_bounds('EX_cpd00092_e0',-1000,1000) #Uracil

GM17.change_bounds('EX_cpd00099_e0',-1000,1000) #Cl-

GM17.change_bounds('EX_cpd00107_e0',-10,1000) #Leucine
GM17.change_bounds('EX_cpd00119_e0',-10,1000) #Histidine

GM17.change_bounds('EX_cpd00126_e0',-1000,1000) #GMP

GM17.change_bounds('EX_cpd00129_e0',-10,1000) #Proline

GM17.change_bounds('EX_cpd00132_e0',-10,1000) #Asparagine

GM17.change_bounds('EX_cpd00149_e0',-1000,1000) #Co2+

GM17.change_bounds('EX_cpd00156_e0',-10,1000) #Valine
GM17.change_bounds('EX_cpd00161_e0',-10,1000) #Threonine

GM17.change_bounds('EX_cpd00182_e0',-1000,1000) #Adenosine
GM17.change_bounds('EX_cpd00184_e0',-1000,1000) #Thymidine

GM17.change_bounds('EX_cpd00205_e0',-1000,1000) #K+

GM17.change_bounds('EX_cpd00215_e0',-1000,1000) #Pyridoxal
GM17.change_bounds('EX_cpd00218_e0',-1000,1000) #Niacin
GM17.change_bounds('EX_cpd00220_e0',-1000,1000) #Riboflavin
GM17.change_bounds('EX_cpd00226_e0',-1000,1000) #HYXN

GM17.change_bounds('EX_cpd00239_e0',-1000,1000) #H2S

GM17.change_bounds('EX_cpd00244_e0',-1000,1000) #Ni2+

GM17.change_bounds('EX_cpd00246_e0',-1000,1000) #Inosine
GM17.change_bounds('EX_cpd00249_e0',-1000,1000) #Uridine

GM17.change_bounds('EX_cpd00254_e0',-1000,1000) #Mg

GM17.change_bounds('EX_cpd00311_e0',-1000,1000) #Guanosine

GM17.change_bounds('EX_cpd00322_e0',-10,1000) #Isoleucine
GM17.change_bounds('EX_cpd00381_e0',-10,1000) #Cystine

GM17.change_bounds('EX_cpd00393_e0',-1000,1000) #Folate
GM17.change_bounds('EX_cpd00438_e0',-1000,1000) #Deoxyadenosine

GM17.change_bounds('EX_cpd00531_e0',-1000,1000) #Hg2+

GM17.change_bounds('EX_cpd00541_e0',-1000,1000) #Lipoate

GM17.change_bounds('EX_cpd00644_e0',-1000,1000) #PAN Pantothenate
GM17.change_bounds('EX_cpd00654_e0',-1000,1000) #Deoxycytidine
GM17.change_bounds('EX_cpd00793_e0',-1000,1000) #Thiamine phosphate

GM17.change_bounds('EX_cpd00971_e0',-1000,1000) #Na+
GM17.change_bounds('EX_cpd01012_e0',-1000,1000) #Cd2+

GM17.change_bounds('EX_cpd01048_e0',-1000,1000) #Arsenate

GM17.change_bounds('EX_cpd03424_e0',-1000,1000) #Vitamin B12

GM17.change_bounds('EX_cpd10515_e0',-1000,1000) #Fe2+
GM17.change_bounds('EX_cpd10516_e0',-1000,1000) #Fe3+

GM17.change_bounds('EX_cpd11574_e0',-1000,1000) #Molybdate
GM17.change_bounds('EX_cpd11595_e0',-1000,1000) #Chromate
GM17.change_bounds('EX_cpd11657_e0',-1000,1000) #Starch



#AP49
AP49.change_bounds('EX_cpd00027_e0',-0.637,1000) #####Glucose

AP49.change_bounds('EX_cpd00001_e0',-1000,1000) #H2O
AP49.change_bounds('EX_cpd00007_e0',-1000,1000) #O2
AP49.change_bounds('EX_cpd00009_e0',-1000,1000) #Phosphate
AP49.change_bounds('EX_cpd00013_e0',-1000,1000) #NH3

AP49.change_bounds('EX_cpd00018_e0',-1000,1000) #AMP
AP49.change_bounds('EX_cpd00020_e0',-1000,1000) #Pyruvate

AP49.change_bounds('EX_cpd00023_e0',-0.637,1000) #####Glutamate

AP49.change_bounds('EX_cpd00028_e0',-1000,1000) # #Heme

AP49.change_bounds('EX_cpd00030_e0',-1000,1000) #Mn2+

AP49.change_bounds('EX_cpd00033_e0',-0.637,1000) #####Glycine

AP49.change_bounds('EX_cpd00034_e0',-1000,1000) #Zn2+

AP49.change_bounds('EX_cpd00035_e0',-0.637,1000) #####Alanine
AP49.change_bounds('EX_cpd00039_e0',-0.637,1000) #####Lysine
AP49.change_bounds('EX_cpd00041_e0',-0.637,1000) #####Aspartate

AP49.change_bounds('EX_cpd00046_e0',-1000,1000) #CMP

AP49.change_bounds('EX_cpd00048_e0',-1000,1000) #Sulfate

AP49.change_bounds('EX_cpd00051_e0',-0.637,1000) #####Arginine

AP49.change_bounds('EX_cpd00053_e0',-0.637,1000) #####Glutamine

AP49.change_bounds('EX_cpd00054_e0',-0.637,1000) #####Serine

AP49.change_bounds('EX_cpd00058_e0',-1000,1000) #Cu2+

AP49.change_bounds('EX_cpd00060_e0',-0.637,1000) #####Methionine

AP49.change_bounds('EX_cpd00063_e0',-1000,1000) #Ca2+

AP49.change_bounds('EX_cpd00065_e0',-0.637,1000) #####Tryptophan
AP49.change_bounds('EX_cpd00066_e0',-0.637,1000) #####Phenylalanine

AP49.change_bounds('EX_cpd00067_e0',-1000,1000) #H+

AP49.change_bounds('EX_cpd00069_e0',-0.637,1000) #####Tyrosine

AP49.change_bounds('EX_cpd00084_e0',-0.637,1000) #####Cysteine

AP49.change_bounds('EX_cpd00091_e0',-1000,1000) #UMP
AP49.change_bounds('EX_cpd00092_e0',-1000,1000) #Uracil

AP49.change_bounds('EX_cpd00099_e0',-1000,1000) #Cl-

AP49.change_bounds('EX_cpd00107_e0',-0.637,1000) #####Leucine
AP49.change_bounds('EX_cpd00119_e0',-0.637,1000) #####Histidine

AP49.change_bounds('EX_cpd00126_e0',-1000,1000) #GMP

AP49.change_bounds('EX_cpd00129_e0',-0.637,1000) #####Proline

AP49.change_bounds('EX_cpd00132_e0',-0.637,1000) #####Asparagine

AP49.change_bounds('EX_cpd00149_e0',-1000,1000) #Co2+

AP49.change_bounds('EX_cpd00156_e0',-0.637,1000) #####Valine
AP49.change_bounds('EX_cpd00161_e0',-0.637,1000) #####Threonine

AP49.change_bounds('EX_cpd00182_e0',-1000,1000) #Adenosine
AP49.change_bounds('EX_cpd00184_e0',-1000,1000) #Thymidine

AP49.change_bounds('EX_cpd00205_e0',-1000,1000) #K+

AP49.change_bounds('EX_cpd00215_e0',-1000,1000) #Pyridoxal
AP49.change_bounds('EX_cpd00218_e0',-1000,1000) #Niacin
AP49.change_bounds('EX_cpd00220_e0',-1000,1000) #Riboflavin
AP49.change_bounds('EX_cpd00226_e0',-1000,1000) #HYXN

AP49.change_bounds('EX_cpd00239_e0',-1000,1000) #H2S

AP49.change_bounds('EX_cpd00244_e0',-1000,1000) #Ni2+

AP49.change_bounds('EX_cpd00246_e0',-1000,1000) #Inosine
AP49.change_bounds('EX_cpd00249_e0',-1000,1000) #Uridine

AP49.change_bounds('EX_cpd00254_e0',-1000,1000) #Mg

AP49.change_bounds('EX_cpd00311_e0',-1000,1000) #Guanosine

AP49.change_bounds('EX_cpd00322_e0',-0.637,1000) #####Isoleucine
AP49.change_bounds('EX_cpd00381_e0',-0.637,1000) #####Cystine

AP49.change_bounds('EX_cpd00393_e0',-1000,1000) #Folate
AP49.change_bounds('EX_cpd00438_e0',-1000,1000) #Deoxyadenosine

AP49.change_bounds('EX_cpd00531_e0',-1000,1000) #Hg2+

AP49.change_bounds('EX_cpd00541_e0',-1000,1000) #Lipoate

AP49.change_bounds('EX_cpd00644_e0',-1000,1000) #PAN Pantothenate
AP49.change_bounds('EX_cpd00654_e0',-1000,1000) #Deoxycytidine
AP49.change_bounds('EX_cpd00793_e0',-1000,1000) #Thiamine phosphate

AP49.change_bounds('EX_cpd00971_e0',-1000,1000) #Na+
AP49.change_bounds('EX_cpd01012_e0',-1000,1000) #Cd2+

AP49.change_bounds('EX_cpd01048_e0',-1000,1000) #Arsenate

AP49.change_bounds('EX_cpd03424_e0',-1000,1000) #Vitamin B12

AP49.change_bounds('EX_cpd10515_e0',-1000,1000) #Fe2+
AP49.change_bounds('EX_cpd10516_e0',-1000,1000) #Fe3+

AP49.change_bounds('EX_cpd11574_e0',-1000,1000) #Molybdate
AP49.change_bounds('EX_cpd11595_e0',-1000,1000) #Chromate
AP49.change_bounds('EX_cpd11657_e0',-1000,1000) #Starch




# YR343-GM17-AP49 = 1-1000-1 (GM17-YR343-AP49 = 1 - 0.001 - 0.001)
YR343.initial_pop=[0,0,3.9e-10]

GM17.initial_pop=[0,0,3.9e-7]

AP49.initial_pop=[0,0,3.9e-10]


test_tube=c.layout()
test_tube.add_model(YR343)
test_tube.add_model(GM17)
test_tube.add_model(AP49)


#R2A Medium Environment
test_tube.set_specific_metabolite('cpd00027_e0', 0.027753108) #Glucose

test_tube.set_specific_metabolite('cpd00001_e0', 1000) #H2O
test_tube.set_specific_metabolite('cpd00007_e0', 1000) #O2
test_tube.set_specific_metabolite('cpd00009_e0', 1000) #Phosphate
test_tube.set_specific_metabolite('cpd00013_e0', 1000) #NH3

#test_tube.set_specific_metabolite('cpd00018_e0', 1000) #AMP

#test_tube.set_specific_metabolite('cpd00020_e0', 1000) #Pyruvate

test_tube.set_specific_metabolite('cpd00023_e0', 0.004892368) #Glutamate 21AA

test_tube.set_specific_metabolite('cpd00028_e0', 1000) # #Heme

test_tube.set_specific_metabolite('cpd00030_e0', 1000) #Mn2+

test_tube.set_specific_metabolite('cpd00033_e0', 0.00952381) #Glycine 21AA

test_tube.set_specific_metabolite('cpd00034_e0', 1000) #Zn2+

test_tube.set_specific_metabolite('cpd00035_e0', 0.008025682) #Alanine 21AA
test_tube.set_specific_metabolite('cpd00039_e0', 0.004859086) #Lysine 21AA
test_tube.set_specific_metabolite('cpd00041_e0', 0.005411255) #Aspartate 21AA

#test_tube.set_specific_metabolite('cpd00046_e0', 1000) #CMP

test_tube.set_specific_metabolite('cpd00048_e0', 1000) #Sulfate

test_tube.set_specific_metabolite('cpd00051_e0', 0.004081633) #Arginine 21AA

test_tube.set_specific_metabolite('cpd00053_e0', 0.004892368) #Glutamine 21AA

test_tube.set_specific_metabolite('cpd00054_e0', 0.006802721) #Serine 21AA

test_tube.set_specific_metabolite('cpd00058_e0', 1000) #Cu2+

test_tube.set_specific_metabolite('cpd00060_e0', 0.004793864) #Methionine 21AA

test_tube.set_specific_metabolite('cpd00063_e0', 1000) #Ca2+

test_tube.set_specific_metabolite('cpd00065_e0', 0.003501401) #Tryptophan 21AA
test_tube.set_specific_metabolite('cpd00066_e0', 0.004329004) #Phenylalanine 21AA

test_tube.set_specific_metabolite('cpd00067_e0', 1000) #H+

test_tube.set_specific_metabolite('cpd00069_e0', 0.00394633) #Tyrosine 21AA

test_tube.set_specific_metabolite('cpd00084_e0', 0.005903188) #Cysteine 21AA

#test_tube.set_specific_metabolite('cpd00091_e0', 1000) #UMP

test_tube.set_specific_metabolite('cpd00092_e0', 1000) # # Uracil

test_tube.set_specific_metabolite('cpd00099_e0', 1000) #Cl-

test_tube.set_specific_metabolite('cpd00107_e0', 0.005452563) #Leucine 21AA
test_tube.set_specific_metabolite('cpd00119_e0', 0.004608295) #Histidine 21AA

#test_tube.set_specific_metabolite('cpd00126_e0', 1000) #GMP

test_tube.set_specific_metabolite('cpd00129_e0', 0.006265664) #Proline 21AA

test_tube.set_specific_metabolite('cpd00132_e0', 0.005411255) #Asparagine 21AA

test_tube.set_specific_metabolite('cpd00149_e0', 1000) #Co2+

test_tube.set_specific_metabolite('cpd00156_e0', 0.006105006) #Valine 21AA
test_tube.set_specific_metabolite('cpd00161_e0', 0.006002401) #Threonine 21AA

test_tube.set_specific_metabolite('cpd00182_e0', 1000) # #Adenosine
test_tube.set_specific_metabolite('cpd00184_e0', 1000) # #Thymidine

test_tube.set_specific_metabolite('cpd00205_e0', 1000) #K+

test_tube.set_specific_metabolite('cpd00215_e0', 1000) # #Pyridoxal
test_tube.set_specific_metabolite('cpd00218_e0', 1000) # #Niacin
test_tube.set_specific_metabolite('cpd00220_e0', 1000) # #Riboflavin
test_tube.set_specific_metabolite('cpd00226_e0', 1000) # #HYXN Hypoxanthine

#test_tube.set_specific_metabolite('cpd00239_e0', 1000) #H2S

test_tube.set_specific_metabolite('cpd00244_e0', 1000) #Ni2+

test_tube.set_specific_metabolite('cpd00246_e0', 1000) # #Inosine
test_tube.set_specific_metabolite('cpd00249_e0', 1000) # #Uridine

test_tube.set_specific_metabolite('cpd00254_e0', 1000) #Mg

test_tube.set_specific_metabolite('cpd00311_e0', 1000) # #Guanosine

test_tube.set_specific_metabolite('cpd00322_e0', 0.005452563) #Isoleucine 21AA
test_tube.set_specific_metabolite('cpd00381_e0', 0.00297619) #Cystine 21AA

test_tube.set_specific_metabolite('cpd00393_e0', 1000) # #Folate
test_tube.set_specific_metabolite('cpd00438_e0', 1000) # #Deoxyadenosine

test_tube.set_specific_metabolite('cpd00531_e0', 1000) #Hg2+

#test_tube.set_specific_metabolite('cpd00541_e0', 1000) #Lipoate

test_tube.set_specific_metabolite('cpd00644_e0', 1000) # #PAN Pantothenate
test_tube.set_specific_metabolite('cpd00654_e0', 1000) # #Deoxycytidine
test_tube.set_specific_metabolite('cpd00793_e0', 1000) # #Thiamine phosphate

test_tube.set_specific_metabolite('cpd00971_e0', 1000) #Na+
test_tube.set_specific_metabolite('cpd01012_e0', 1000) #Cd2+

#test_tube.set_specific_metabolite('cpd01048_e0', 1000) #Arsenate

test_tube.set_specific_metabolite('cpd03424_e0', 1000) # #Vitamin B12

test_tube.set_specific_metabolite('cpd10515_e0', 1000) #Fe2+
test_tube.set_specific_metabolite('cpd10516_e0', 1000) #Fe3+

#test_tube.set_specific_metabolite('cpd11574_e0', 1000) #Molybdate
#test_tube.set_specific_metabolite('cpd11595_e0', 1000) #chromate
#test_tube.set_specific_metabolite('cpd11657_e0', 1000) #Starch




comp_params = c.params()
comp_params.set_param('maxCycles',960) #### to change

comp_params.set_param('defaultVmax',10) #### to change
comp_params.set_param('defaultKm',0.01)

comp_params.set_param('exchangestyle','Monod Style')

comp_params.set_param('timeStep',0.05) #### to change

comp_params.set_param('spaceWidth',2.1544)

comp_params.set_param('maxSpaceBiomass',1000)
comp_params.set_param('minSpaceBiomass',1e-11)

comp_params.set_param('defaultHill',1)

comp_params.set_param('writeMediaLog',True)
comp_params.set_param('writeFluxLog',True)
comp_params.set_param('MediaLogRate',1)
comp_params.set_param('FluxLogRate',1)

comp_params.set_param('writeTotalBiomassLog',True)
comp_params.set_param('writeBiomassLog',True)
comp_params.set_param('totalBiomassLogRate',1)
comp_params.set_param('BiomassLogRate',1)

comp_params.set_param("writeSpecificMediaLog", True)
comp_params.set_param("specificMediaLogRate", 1) 
comp_params.set_param("specificMedia", "cpd00027_e0")

comp_params.set_param('deathRate',0)

one_cell=3.9e-13 # gram dry weight of a cell

comp_assay=c.comets(test_tube,comp_params)
comp_assay.run()



serial_params=c.params()
serial_params.set_param('maxCycles',960*6) #### to change
serial_params.set_param('batchDilution',True)

serial_params.set_param('dilFactor',0.1)

serial_params.set_param('dilTime',48)

serial_params.set_param('defaultVmax',10) #### to change
serial_params.set_param('defaultKm',0.01)

serial_params.set_param('exchangestyle','Monod Style')

serial_params.set_param('timeStep',0.05) #### to change

serial_params.set_param('spaceWidth',2.1544)

serial_params.set_param('maxSpaceBiomass',1000)
serial_params.set_param('minSpaceBiomass',1e-11)

serial_params.set_param('defaultHill',1)

serial_params.set_param('writeMediaLog',True)
serial_params.set_param('writeFluxLog',True)
serial_params.set_param('MediaLogRate',1)
serial_params.set_param('FluxLogRate',1)

serial_params.set_param('writeTotalBiomassLog',True)
serial_params.set_param('writeBiomassLog',True)
serial_params.set_param('totalBiomassLogRate',1)
serial_params.set_param('BiomassLogRate',1)

serial_params.set_param('deathRate',0)

one_cell=3.9e-13 # gram dry weight of a cell

serial_expt=c.comets(test_tube,serial_params)
serial_expt.run()











