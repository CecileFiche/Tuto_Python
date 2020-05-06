# A METTRE DANS LE FICHIER CONFIG

import sys
sys.path.append('/home/fiche/Workspace/Python/Tuto_Python/Test_Project/')

from os import system
from Test_Project.Model.Experiment.daq_experiment import DAQ_Experiment
from Test_Project.View.main_window import Ui_MainWindow

from PyQt5 import QtWidgets

system('clear')

app = QtWidgets.QApplication(sys.argv)
m = Ui_MainWindow() # Instentiation of the class Ui_MainWindow()
m.setupUi(m) # Apply the method setupUi
    
m.show()
app.exit(app.exec_())