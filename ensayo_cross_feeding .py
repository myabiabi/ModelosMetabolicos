##Procedure 2: simulating cross-feeding in a chemostat ● Timing setup: 30 min to 1 h, simulation: 1–5 min

###importar paquetes requeridos
###modelo de e. coli iJO1366
import cobra
import cobra.io 
import cometspy as c 
from matplotlib import pyplot as plt 
import pandas as pd

E_no_galE = cobra.io.load_model("iJO1366") #cobra.io.load_model no lee bases de datos desde los archivos, lee ID 

E_no_LCTStex = E_no_galE.copy() #El modelo de e. coli que no puede absorber lactosa puede mantenerse en un quimiostato 
#al que sólo se le suministra lactosa, cuando está presente otra cepa que puede metabolizar la lactosa pero que no puede 
# #metabolizar el monómero de galactosa.

E_no_galE.genes.b0759.knock_out() #crear sepa que metaboliza lactosa pero no monomero de galactosa

E_no_LCTStex.reactions.LCTStex.knock_out() #no puede consumir lacotosa

#cambiar id de los modelos 

E_no_galE.id = "galE_KO"  #no metaboliza galactosa
E_no_LCTStex.id = "LCTStex_KO" #no consume lactosa
#hacer un modelo COMETS de un modelo COBRA 
galE_comets = c.model(E_no_galE) #no metaboliza galactosa
lcts_comets = c.model(E_no_LCTStex)#no consume lactosa

#biomasa inicial
#los modelos de comets deben tener una biomasa inicial
#atributos de ''initial_pop'': 
#x: location
#y: location
#tamaño de la población en gramos en peso seco (gDW)
initial_pop = 1.e-3 #gDW
#initial pop debe ser positivo
galE_comets.initial_pop = [0,0,initial_pop] #x, y, gDW
lcts_comets.initial_pop = [0,0,initial_pop] #x, y, gDW

#abrir exchange bounds
#En las simulaciones de COMETS, las concentraciones de metabolitos 
#deberían determinar los límites de intercambio
galE_comets.open_exchanges() #abre todos los intercambios, default lower_bound = -1000, upper_bound = 1000
lcts_comets.open_exchanges()

#metodo para optimizar 
#maximiza la biomasa 
#minimiza el totoal de flujos 
galE_comets.obj_style = "MAX_OBJECTIVE_MIN_TOTAL"
lcts_comets.obj_style = "MAX_OBJECTIVE_MIN_TOTAL"

#carga el modelo en un objeto COMETS, da la estructura con una lista de modelos COMETS 
layout = c.layout([galE_comets, lcts_comets])
#las simulaciones COMETS corrern 1 a 1
#cambiar este atributo covierte la simulacion de una ambiente bien mezclado a un ambiente espacial

#especificar metabolitos en el layout 
unlimited_mets = ['ca2_e', 'cl_e', 'co2_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e','h_e', 
                  'h2o_e', 'k_e', 'mg2_e', 'mn2_e', 'mobd_e', 'na1_e', 'nh4_e', 'ni2_e','o2_e', 
                  'pi_e', 'sel_e', 'slnt_e', 'so4_e', 'tungs_e', 'zn2_e'] 

for met in unlimited_mets: 
    layout.set_specific_metabolite(met, 1000.) 
    layout.set_specific_metabolite("lcts_e", 1.)
#asigna 1000 mmol a todos los metabolitos ilimitados y 1 mmmol a la lactosa
#el layout debe tener metaboliros para que el modelo sea capaz de crecer 


####el quimiostato requiere metabolitos para que se ''refresque'' (actualizada'')
##Dada una tasa de dilución de 0,1 (por hora), esta es una tasa de actualización 
#de 100 mmol/h/caja para los metabolitos ilimitados y 0,1 mmol/h/caja para la lactosa.

dilution_rate = 0.1 # / hr 
for met in unlimited_mets: 
    layout.set_specific_refresh(met, 1000. * dilution_rate) # 100 mmol / hour 
    layout.set_specific_refresh("lcts_e", 1. * dilution_rate) # 0.1 mmol / hour
#esto es lo que hace que el la simulación este en flujo 
#EL LAYOUT ESTA COMPLETO 

#especificar parametrros

params = c.params()


params.set_param("deathRate", dilution_rate) #para determinar la tasa en la uqe se pierde biomasa del sistema 
#la tasa de dilución crea la salida del quimiostato
params.set_param("metaboliteDilutionRate", dilution_rate)



params.set_param("spaceWidth", 0.1) 
params.set_param("defaultVmax", 15.) 
params.set_param("defaultKm", 0.0001)

params.set_param("timeStep", 0.1) 
params.set_param("maxSpaceBiomass", 10.) 
params.set_param("maxCycles", 300)

params.set_param("writeFluxLog", True) 
params.set_param("writeMediaLog", True) 
params.set_param("FluxLogRate", 1) 
params.set_param("MediaLogRate", 1)

sim = c.comets(layout, params)
sim.run()


##############FIGURAS###############
import os
import matplotlib.pyplot as plt
##
sim.total_biomass.plot(x = "cycle")

plt.ylabel("biomass (gDW)")

media = sim.get_metabolite_time_series(upper_threshold = 900.) 
media.plot(x = "cycle") 
plt.ylabel("mmol")


output_folder = 'graficas'
output_path = os.path.join(output_folder, 'biomasa.png')
plt.savefig(output_path)

###########hasat aqui todo bien

LCTStex_KO_flux = sim.get_species_exchange_fluxes("LCTStex_KO", threshold = 1.) #en el ejemplo el threshold es 5 pero era un valor muy alto y no garficaba nada
#Utilice el argumento opcional th3reshold para determinar el valor absoluto mínimo de flujo que una reacción de intercambio logró para retener solo flujos de intercambio sustanciales 
#(es decir, para excluir flujos de pequeña magnitud de minerales traza)
galE_KO_flux = sim.get_species_exchange_fluxes("galE_KO", threshold = 1.)


output_folder = 'graficas'
output_path = os.path.join(output_folder, 'metabolitos.png')
plt.savefig(output_path)


#################3
ignoreable_exchanges = ["EX_ac_e", "EX_co2_e", "EX_o2_e"] 
LCTStex_KO_flux = LCTStex_KO_flux.drop(ignoreable_exchanges, axis = 1) 
galE_KO_flux = galE_KO_flux.drop(ignoreable_exchanges, axis = 1) 
plt.rcParams["figure.figsize"] = (10,5) 
fig, ax = plt.subplots(1,2) 

##El método .plot() de un DataFrame de pandas no acepta title directamente como argumento.
#######3########fghjk
galE_KO_flux.plot(x= "cycle", ax=ax[0])
ax[0].set_title("galE_KO")

LCTStex_KO_flux.plot(x= "cycle", ax=ax[1])
ax[1].set_title("LCTStex_KO")


output_folder = 'graficas'
output_path = os.path.join(output_folder, 'flujos1.png')
plt.savefig(output_path)


plt.show()