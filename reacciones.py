import cobra

# Assuming you have a model loaded, e.g., from a file
# Replace "your_model.xml" with the actual path to your model file

#ruta_C2R = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM_1/gps_C2R.xml'
model_C2R_gps = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM_1/gps_C2R.xml')

# Get the list of reactions
reactions = model_C2R_gps.reactions

# Print the IDs of the reactions
for reaction in reactions:
    print(reaction.id)

# You can also access other properties of each reaction
for reaction in reactions:
    print(f"Reaction ID: {reaction.id}")
    print(f"  Equation: {reaction.reaction}")
    print(f"  Lower bound: {reaction.lower_bound}")
    print(f"  Upper bound: {reaction.upper_bound}")
    print("-" * 20)



#ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM_1/gps_RC3.xml'
model_RC3_gps = cobra.io.read_sbml_model('/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM_1/gps_RC3.xml')
# Get the list of reactions
reactions = model_C2R_gps.reactions

# Print the IDs of the reactions
for reaction in reactions:
    print(reaction.id)

# You can also access other properties of each reaction
for reaction in reactions:
    print(f"Reaction ID: {reaction.id}")
    print(f"  Equation: {reaction.reaction}")
    print(f"  Lower bound: {reaction.lower_bound}")
    print(f"  Upper bound: {reaction.upper_bound}")
    print("-" * 20)
