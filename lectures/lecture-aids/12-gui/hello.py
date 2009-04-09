import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
widget = QtGui.QLabel('Hello World')
widget.setWindowTitle('Hello')
widget.show()
sys.exit(app.exec_())

