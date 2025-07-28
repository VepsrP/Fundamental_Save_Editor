# This Python file uses the following encoding: utf-8
import sys, base64

from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    loadfile = ""
    savefile = ""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadFile.clicked.connect(self.LoadFile)

    def LoadFile(self):
        text:str = ""
        self.loadfile = QtWidgets.QFileDialog.getOpenFileName(self, "Open Save File", "/", filter="*.txt")
        with open(self.loadfile[0], 'r') as lf:
            text = lf.read()
        text = base64.b64decode(text).decode('utf-8')
        print(text)
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
