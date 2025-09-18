#Reacciones de cada modelo
import cometspy as c
import cobra.io
#Pseudomonas umsongensis
ST00042_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve42.xml')
ST00042_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00042_diamon.xml')
ST00042_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00042dd.xml')
print(len(ST00042_.exchanges))
print(len(ST00042_d.exchanges))
print(len(ST00042_dd.exchanges))
#Bacillus
ST00046_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve46.xml')
ST00046_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00046_diamon.xml')
ST00046_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00046dd.xml')
print(len(ST00046_.exchanges))
print(len(ST00046_d.exchanges))
print(len(ST00046_dd.exchanges))
#Arthrobacter
ST00060_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve60.xml')
ST00060_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00060_diamon.xml')
ST00060_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00060dd.xml')
print(len(ST00060_.exchanges))
print(len(ST00060_d.exchanges))
print(len(ST00060_dd.exchanges))
#Mycobacterium
ST00109_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve109.xml')
ST00109_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00109_diamon.xml')
ST00109_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00109dd.xml')
print(len(ST00109_.exchanges))
print(len(ST00109_d.exchanges))
print(len(ST00109_dd.exchanges))
#Paenibacillus
ST00143_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve143.xml')
ST00143_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00143_diamon.xml')
ST00143_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00143dd.xml')
print(len(ST00143_.exchanges))
print(len(ST00143_d.exchanges))
print(len(ST00143_dd.exchanges))
#Agrobacterium
ST00154_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve154.xml')
ST00154_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00154_diamon.xml')
ST00154_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00154dd.xml')
print(len(ST00154_.exchanges))
print(len(ST00154_d.exchanges))
print(len(ST00154_dd.exchanges))
#Bacillus thuringensis
ST00164_ = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DEFAULT/carve164.xml')
ST00164_d = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT/ST00164_diamon.xml')
ST00164_dd = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/01_data/models_carveme/DIAMONT_2/ST00164dd.xml')
print(len(ST00164_.exchanges))
print(len(ST00164_d.exchanges))
print(len(ST00164_dd.exchanges))


