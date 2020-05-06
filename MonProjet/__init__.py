# coding: utf-8

import logging, yaml
import os.path as path
import warnings

warnings.filterwarnings("ignore")

# Configuration pour les bases de données

#<-- Non, on fait pas comme ça, on fait un chemin absolu cf. __init__.py -->
# sys.path.append('/home/fiche/Workspace/Python/Tuto_Python/Test_Project/')

# comme ici :
config_test = yaml.load(open(path.join(path.dirname(__file__), "config_test.dist.yml")))
examples_path = path.abspath(config_test['examples'])