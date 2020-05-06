# A METTRE DANS LE FICHIER CONFIG

from MonProjet.Test_Project.Model.Experiment.daq_experiment import DAQ_Experiment
from MonProjet.Test_Project.View.main_window import Ui_MainWindow

import os.path as path
from MonProjet import config_test, examples_path
import sys
from os import system
from PyQt5 import QtWidgets


# sys.path.append('/home/fiche/Workspace/Python/Tuto_Python/Test_Project/') <-- Non, on fait un chemin absolu cf. __init__.py

print("LAAA : {}".format(examples_path))

system('clear')

app = QtWidgets.QApplication(sys.argv)
m = Ui_MainWindow() # Instentiation of the class Ui_MainWindow()
m.setupUi(m) # Apply the method setupUi
    
m.show()
app.exit(app.exec_())