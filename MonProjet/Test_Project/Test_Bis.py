
# A METTRE DANS LE FICHIER CONFIG

from MonProjet.Test_Project.Model.Experiment.daq_experiment import DAQ_Experiment
from MonProjet.Test_Project.View.main_window import Ui_MainWindow

import os.path as path
import ressources_path, config_test
import sys
from os import system
from PyQt5 import QtWidgets

system('clear')

app = QtWidgets.QApplication(sys.argv)
m = Ui_MainWindow() # Instentiation of the class Ui_MainWindow()
m.setupUi(m) # Apply the method setupUi
    
m.show()
app.exit(app.exec_())