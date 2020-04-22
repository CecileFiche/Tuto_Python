import yaml

def load_config(filename):
	with open(filename, 'r') as f:
		data = yaml.load(f, Loader=yaml.FullLoader)

	return data