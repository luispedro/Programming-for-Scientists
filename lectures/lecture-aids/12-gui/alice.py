import sys
from PyQt4 import QtGui, QtCore
app = QtGui.QApplication(sys.argv)

button = QtGui.QPushButton('Press Me')
button.setWindowTitle('Hello')
button.show()

bigger = True
def resize():
    global bigger
    w = button.width()
    h = button.height()
    if bigger:
        button.resize(w*2,h*2)
    else:
        button.resize(w//2,h//2)
    bigger = not bigger


app.connect(button, QtCore.SIGNAL('clicked()'), resize)
sys.exit(app.exec_())

