import sys
import os
sys.path.append(r"C:\Python27\Lib\site-packages")
sys.path.append(r"C:\Program Files\Autodesk\Maya2020\Python\Lib\site-packages")
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)
        self.setWindowTitle("Test Dialog")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(200)
        self.create_widgets()
        self.create_layouts()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox("CheckBox1")
        self.checkbox2 = QtWidgets.QCheckBox("CheckBox2")
        self.button1 = QtWidgets.QPushButton("Button1")
        self.button2 = QtWidgets.QPushButton("Button2")

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox1)
        main_layout.addWidget(self.checkbox2)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)

if __name__ == "__main__":
    d = TestDialog()
    d.show()
