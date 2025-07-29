# This Python file uses the following encoding: utf-8
import sys, base64, json, jsonmodel

from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItem, QStandardItemModel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    loadfile:str = ""
    content = ""
    tree = jsonmodel.JsonModel()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadFile.clicked.connect(self.LoadFile)

    def LoadFile(self) -> None:
        self.loadfile = QtWidgets.QFileDialog.getOpenFileName(self, "Open Save File", "/", filter="*.txt")[0]
        self.savefile = self.loadfile + "1.txt"
        with open(self.loadfile, 'r') as lf:
            self.content = lf.read()
        self.content = base64.b64decode(self.content).decode('utf-8')
        self.content = json.loads(self.content)
        self.tree.load(self.content)
        self.ui.treeView.setModel(self.tree)
        return

    def SaveFile(self) -> None:
        self.content = json.dumps(self.tree.to_json())
        self.content = base64.b64encode(bytes(self.content, "utf-8")).decode("utf-8")
        with open(self.loadfile, 'w') as sf:
            sf.write(self.content)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
