from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class Edit (qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("Edit name"))
        self.name=qt.QLineEdit()
        self.name.setAccessibleName(_("name"))
        self.anser=qt.QCheckBox(_("True anser"))
        self.anser.setChecked(True)
        self.ok=qt.QPushButton(_("add"))
        self.ok.clicked.connect(lambda:self.add(p))
        self.cansel=qt.QPushButton(_("cancel"))
        self.cansel.clicked.connect(lambda:self.close())
        layout=qt.QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.anser)
        layout.addWidget(self.ok)
        layout.addWidget(self.cansel)
        self.setLayout(layout)
    def add(self,p):
        p.names.addItem(_("{} anser: {}").format(self.name.text(),str(self.anser.isChecked())))
        if self.anser.isChecked(): p.True_ansers.append(self.name.text())
        self.close()