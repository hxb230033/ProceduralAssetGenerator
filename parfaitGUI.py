import importlib


from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui

import parfait
importlib.reload(parfait)
from parfait import Parfait, FLAVORS


def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)


class ParfaitGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_main_maya_win())
        self.parfait_generator = Parfait()
        self.setWindowTitle("Procedural Parfait")
        self.setWindowFlag(QtCore.Qt.WindowType.Tool)
        self.create_layout()
        self.create_connections()
    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()

        self.glass_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.glass_size_dspnbx.setRange(0.5, 5.0)
        self.glass_size_dspnbx.setSingleStep(0.5)
        self.glass_size_dspnbx.setValue(self.parfait_generator.glass_size)
        self.form_lay.addRow("Glass Size", self.glass_size_dspnbx)

        self.scoops_spnbx = QtWidgets.QSpinBox()
        self.scoops_spnbx.setRange(1, 5)
        self.scoops_spnbx.setValue(self.parfait_generator.scoop_amount)
        self.form_lay.addRow("Amount of Scoops", self.scoops_spnbx)

        self.flavor_cmbbox = QtWidgets.QComboBox()
        self.flavor_cmbbox.addItems([FLAVORS])
        self.flavor_cmbbox.setCurrentText(self.parfait_generator.flavor)
        self.form_lay.addRow("Flavor", self.flavor_cmbbox)

        self.addcherry_cb = QtWidgets.QCheckBox()
        self.addcherry_cb.setChecked(self.parfait_generator.a)
        self.form_lay.addRow("Add Cherry", self.addcherry_cb)

        self.straws_spnbx = QtWidgets.QSpinBox()
        self.straws_spnbx.setRange(0, 4)
        self.straws_spnbx.setValue(self.parfait_generator.straw_amount)
        self.form_lay.addRow("Amount of Straws", self.straws_spnbx)

        self.enablegrpname_cb = QtWidgets.QCheckBox()
        self.enablegrpname_cb.setChecked(False)
        self.form_lay.addRow("Enable Group Name", self.enablegrpname_cb)
        self.grpname_le = QtWidgets.QLineEdit()
        self.grpname_le.setText(self.parfait_generator.grp_name)
        self.grpname_le.setEnabled(False)
        self.form_lay.addRow("Group Name", self.grpname_le)

        self.main_lay.addLayout(self.form_lay)

    def create_connections(self):
        self.enablegrpname_cb.toggled.connect(self.toggle_grpname_le)
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def toggle_grpname_le(self):
        self.grpname_le.setEnabled(self.enablegrpname_cb.isChecked())
        
    @QtCore.Slot()
    def create(self):
        generate = self.parfait_generator
        generate.glass_size = self.glass_size_dspnbx.value()
        generate.scoop_amount = self.scoops_spnbx.value()
        generate.flavor = self.flavor_cmbbox.currentText()
        generate.add_cherry = self.cherry_cb.isChecked()
        generate.straw_amount = self.straws_spnbx.value()
        if self.enablegrpname_cb.isChecked():
            generate.grpname = self.grpname_le.text()
        generate.create()

gui = ParfaitGUI()
gui.show()