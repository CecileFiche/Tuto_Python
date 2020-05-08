from os import system
import sys
from PyQt5 import QtWidgets

from First_Project.View.main_window import Ui_MainWindow
from First_Project import config_parameters, main_path

system('clear')

app = QtWidgets.QApplication(sys.argv)
m = Ui_MainWindow(config_parameters,main_path) # Instentiation of the class Ui_MainWindow()
m.setupUi(m) # Apply the method setupUi
    
m.show()
app.exit(app.exec_())