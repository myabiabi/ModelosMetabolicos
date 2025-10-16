import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('01_data/models_carveme/prokka/biomasas/ST00109_biomass.csv')
datos2 = pd.read_csv('01_data/models_carveme/prokka/biomasas/ST00143_biomass.csv')

tiempo = datos['cycle']
masa1 = datos['ST00109']
masa2 = datos2['ST00143']
import numpy as np
log_masa = np.log(masa1)
log_masa2 = np.log(masa2)

import numpy as np
plt.figure(figsize=(10, 6))
plt.plot(tiempo, masa1, marker='o', linestyle='-', color='blue', label='masa')
plt.plot(tiempo, masa1, marker='o', linestyle='-', color='pink', label='masa')

plt.title('Curva de Crecimiento Bacteriano')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Densidad Óptica (DO)')
plt.grid(True)
plt.legend()
plt.show()