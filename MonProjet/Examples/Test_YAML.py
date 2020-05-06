import yaml
from os import system
import numpy as np

system('clear')

# Open the yml file and save it in the variable 'e'. This variable is a dictionnary.
# Note that the program is using the 'with' command, which is a more secure and 
# easy way to open file (even if there is an error, the file will be properly closed
# at the end).
# ------------

with open('Config/experiment.yml', 'r') as f:
	e = yaml.load(f, Loader=yaml.FullLoader)

print(e['Experiment'])

# Display each field separatly on the terminal. Each field is indicating by:
# - its name
# - its value
# - the type of the variable (float, int, list, string, etc.)
# - a line composed of ten '-'
# ---------------------------- 

for k in e['Experiment']:
	print(k)
	var = e['Experiment'][k]
	print(var)
	print(type(var))
	print(10*'-')

# Create a new file with a dictionary
# -----------------------------------

system('cd /home/fiche/Desktop/Workspace/Python/Tuto_Python/Examples/')

d = {'Experiment': {
'name': 'test_1',
'range': [1, 10],}
}

with open('data.yml', 'w') as f:
	f.write(yaml.dump(d, default_flow_style=False))

# Append with new data
# --------------------

A = np.array([1, 2, 3])

with open('data.yml', 'r') as f:
	e = yaml.load(f, Loader=yaml.FullLoader)

e['results'] = A

with open('data.yml', 'a') as f:
	f.write(yaml.dump(e, default_flow_style=False))

# Read the new file
# -----------------

with open('data.yml', 'r') as f:
	e = yaml.load(f, Loader=yaml.FullLoader)

print('\n\n\n')

for k in e['Experiment']:
	print(k)
	var = e['Experiment'][k]
	print(var)
	print(type(var))
	print(10*'-')