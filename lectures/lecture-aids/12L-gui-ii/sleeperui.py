import sys
from PyQt4 import QtCore, QtGui
app = QtGui.QApplication(sys.argv)

button = QtGui.QPushButton('Press Me')
button.setWindowTitle('Hello')
button.show()
proc = QtCore.QProcess()

def process_output():
    output = proc.readAllStandardOutput()
    button.setText(str(output).strip())
    print 'output from process >>', output, '<<'

def startit():
    proc.start('python',['sleeper.py','10'])

app.connect(button, QtCore.SIGNAL('clicked()'),startit)
app.connect(proc,QtCore.SIGNAL('readyReadStandardOutput()'),process_output)

sys.exit(app.exec_())
