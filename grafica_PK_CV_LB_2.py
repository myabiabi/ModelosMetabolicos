import pandas as pd
import matplotlib.pyplot as plt
import glob

csv_file_1 = glob.glob('01_data/models_carveme/prokka/biomasas/ST00109_biomass.csv')
csv_file_2 = glob.glob('01_data/models_carveme/prokka/biomasas/ST00143_biomass.csv')


#all_dataframes = []
#for file in csv_files:
        #df = pd.read_csv(file)
        #all_dataframes.append(df)
#print(all_dataframes)





import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Example: Simple competitive growth model for two bacterial strains
#def bacterial_community_growth(N, t, r1, K1, r2, K2, alpha12, alpha21):
    #N1, N2 = N # Population sizes of strain 1 and strain 2
    
    # Logistic growth with competitive inhibition
    ##dN1dt = r1 * N1 * (1 - (N1 + alpha12 * N2) / K1)
    #dN2dt = r2 * N2 * (1 - (N2 + alpha21 * N1) / K2)
    
    #return [dN1dt, dN2dt]

# Parameters
#r1, K1 = 0.5, 1000 # Growth rate and carrying capacity for strain 1
#r2, K2 = 0.4, 800  # Growth rate and carrying capacity for strain 2
#alpha12 = 0.8     # Effect of strain 2 on strain 1
#alpha21 = 0.6     # Effect of strain 1 on strain 2

initial_populations = [10, 5] # Initial populations of N1 and N2
time_points = np.linspace(0, 50, 500) # Time points for simulation

# Solve the differential equations
#solution = odeint(bacterial_community_growth, initial_populations, time_points, 
                   #args=(r1, K1, r2, K2, alpha12, alpha21))

# Extract individual strain populations
#N1_history = solution[:, 0]
#N2_history = solution[:, 1]
#Total_N = N1_history + N2_history

# Plotting the growth curves
plt.figure(figsize=(10, 6))
plt.plot(time_points, N1_history, label='Strain 1 Population')
plt.plot(time_points, N2_history, label='Strain 2 Population')
plt.plot(time_points, Total_N, label='Total Community Population', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Bacterial Community Growth Curve')
plt.legend()
plt.grid(True)
plt.show()