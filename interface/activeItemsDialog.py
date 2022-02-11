from sys import path as sp
from copy import deepcopy as Copy
sp.insert(1,'.')

from PyQt5.QtWidgets import QToolBox, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from interface.activeItemsUi import Ui_ToolBox as ui
from dist import pydist as pd

class ActiveItemsDialog(QToolBox):
    Mainui = ui

    def __init__(self) -> None:
        super().__init__(flags=Qt.WindowType.WindowCloseButtonHint)
        self.Mainui = ui()
        self.Mainui.setupUi(self)

        self.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+"assets/tickathon.png"))
        self.setWindowTitle("Active items")

    def List2ActiveItems(self,full:list[QListWidgetItem]):
        self.Mainui.DoneList.clear()
        self.Mainui.UndoneList.clear()
        for item in full:
            newitem = item.clone()
            newitem.setText(f"({full.index(item)+1}) "+item.text())
            newitem.setFlags(Qt.ItemFlag.ItemIsEnabled)
            if newitem.checkState() == Qt.CheckState.Checked:
                self.Mainui.DoneList.addItem(newitem)
            else:
                self.Mainui.UndoneList.addItem(newitem)

    def Open(self,full:list[QListWidgetItem]):
        self.List2ActiveItems(full)
        self.show()
    
    def Close(self):
        self.close()