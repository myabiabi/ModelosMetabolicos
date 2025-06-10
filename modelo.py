import cometspy as c
import cobra.io
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt


ruta = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/C2RQJT.xml'
ruta2 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/RC3LPC.xml'
# Cargar el modelo usando COBRApy y COMETS
wt1 = c.model(cobra.io.read_sbml_model(ruta))  # Usar la ruta correcta del archivo
wt2 = c.model(cobra.io.read_sbml_model(ruta2)) 



import pandas as pd
