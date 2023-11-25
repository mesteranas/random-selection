import sys
from custome_errors import *
sys.excepthook = my_excepthook
import winsound
import random
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.True_ansers=[]
        self.names=qt.QListWidget()
        self.names.setAccessibleName(_("names"))
        self.names.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.names.customContextMenuRequested.connect(self.oncontext)
        layout.addWidget(self.names)
        self.add=qt.QPushButton(_("add name"))
        self.add.setDefault(True)
        self.add.clicked.connect(lambda: gui.Add(self).exec())
        layout.addWidget(self.add)
        self.choose=qt.QPushButton(_("choose name"))
        self.choose.setDefault(True)
        self.choose.clicked.connect(self.Choos)
        qt1.QShortcut("delete",self).activated.connect(self.fdelete)
        qt1.QShortcut("ctrl+s",self).activated.connect(self.fnor)
        qt1.QShortcut("ctrl+shift+s",self).activated.connect(self.fmol)
        qt1.QShortcut("f2",self).activated.connect(lambda:gui.Edit(self).exec())
        layout.addWidget(self.choose)
        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def Choos(self):
        m=qt.QMenu(_("select choose mode"))
        normal=qt1.QAction(_("choose name"),self)
        m.addAction(normal)
        normal.triggered.connect(self.fnor)
        mol=qt1.QAction(_("choose multable names"),self)
        m.addAction(mol)
        mol.triggered.connect(self.fmol)
        m.exec()
    def fnor(self):
        try:
            qt.QMessageBox.information(self,_("congratulation"),_("the winner is {}").format(random.choice(self.True_ansers)))
            winsound.PlaySound("data/sounds/1.wav",1)
        except:
            qt.QMessageBox.information(self,_("error"),_("please add name fristly"))
    def fmol(self):
        count,ok=qt.QInputDialog.getInt(self,_("choose"),_("type names count  to choose"),2,2,30,1)
        if ok:
            try:
                qt.QMessageBox.information(self,_("congratulation"),_("the winner are {}").format(",".join(random.sample(self.True_ansers,count))))
                winsound.PlaySound("data/sounds/1.wav",1)
            except:
                qt.QMessageBox.information(self,_("error"),_("please add names fristly"))
    def oncontext(self,pos):
        if self.names.count()==0:
            guiTools.speak("please add names fristly")
        else:
            m=qt.QMenu(_("context"))
            delete=qt1.QAction(_("delete"),self)
            m.addAction(delete)
            delete.triggered.connect(self.fdelete)
            edit=qt1.QAction(_("edit"),self)
            m.addAction(edit)
            edit.triggered.connect(lambda:gui.Edit(self).exec())
            m.exec()
    def fdelete(self):
        try:
            a=self.names.currentItem().text()
            self.names.takeItem(self.names.row(self.names.currentItem()))
            try:
                self.True_ansers.remove(a.split(_(" anser: "))[0])
            except: pass
            guiTools.speak(_("deleted"))
        except: guiTools.speak(_("error"))

App=qt.QApplication([])
w=main()
w.show()
App.exec()