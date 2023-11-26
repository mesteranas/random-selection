import guiTools
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
        self.ok=qt.QPushButton(_("edit"))
        self.ok.clicked.connect(lambda:self.add(p))
        self.cansel=qt.QPushButton(_("cancel"))
        self.cansel.clicked.connect(lambda:self.close())
        layout=qt.QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.anser)
        layout.addWidget(self.ok)
        layout.addWidget(self.cansel)
        self.setLayout(layout)
        try:
            aaa=p.names.currentItem().text().split(" anser: ")
            self.name_=aaa[0]
            self.anser_=settings.cbts(1,aaa[1])
            self.anser.setChecked(self.anser_)
            self.name.setText(self.name_)
        except:
            guiTools.speak(_("error please select item fristly"))
            self.name.setDisabled(True)
            self.anser.setDisabled(True)
            self.ok.setDisabled(True)
            self.close()
    def add(self,p):
        p.names.currentItem().setText(_("{} anser: {}").format(self.name.text(),str(self.anser.isChecked())))
        try:
            p.True_ansers.remove(self.name_)
        except:
            pass
        if self.anser.isChecked(): p.True_ansers.append(self.name.text())
        self.close()