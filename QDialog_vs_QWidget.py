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
        self.setWindowFlags(self.windowFlags()
                            ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(200)
        self.create_widgets()
        self.create_layouts()

        self.create_connections()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox()
        self.checkbox2 = QtWidgets.QCheckBox()
        self.btn_ok = QtWidgets.QPushButton("OK")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")

    def create_layouts(self):
        layout_button = QtWidgets.QHBoxLayout()
        layout_button.addStretch()
        layout_button.addWidget(self.btn_ok)
        layout_button.addWidget(self.btn_cancel)

        layout_form = QtWidgets.QFormLayout()
        layout_form.addRow("Name: ", self.lineedit)
        layout_form.addRow("Hidden: ", self.checkbox1)
        layout_form.addRow("Locked: ", self.checkbox2)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(layout_form)
        main_layout.addLayout(layout_button)

    def create_connections(self):
        self.lineedit.editingFinished.connect(self.print_hello_name)
        self.checkbox1.toggled.connect(self.print_is_hidden)
        self.btn_cancel.clicked.connect(self.close)

    def print_hello_name(self):
        name = self.lineedit.text()
        print("Hello {0}".format(name))

    def print_is_hidden(self):
        hidden = self.checkbox1.isChecked()
        if hidden:
            print("Hidden: ")
        else:
            print("Visible: ")


if __name__ == "__main__":
    try:
        test_dialog.close()  # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
