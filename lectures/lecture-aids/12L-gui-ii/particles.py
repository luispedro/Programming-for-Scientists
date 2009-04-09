import sys
from PyQt4 import QtGui, QtCore
from ui_particles import Ui_MainWindow
app = QtGui.QApplication(sys.argv)

class ParticlesMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    
def doparticles():
    print 'Particles called'
main = ParticlesMainWindow()
app.connect(main.runbutton, QtCore.SIGNAL('clicked()'), doparticles)
app.connect(main.actionQuit,QtCore.SIGNAL('activated()'),app.quit)
main.show()
sys.exit(app.exec_())

