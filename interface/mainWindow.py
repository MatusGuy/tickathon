from sys import path as sp
sp.insert(1,'.')

from PyQt5.QtWidgets import QListWidgetItem,QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, Qt, QModelIndex
from interface.mainUi import Ui_MainWindow as ui

from dist import pydist as pd

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication

    def __init__(self,window:QMainWindow,app:QApplication):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")

        super().__init__()
        super().setupUi(self.window)
        self.InitIcons()

        self.AddAction.triggered.connect(self.AddItem)
        self.RemoveAction.triggered.connect(lambda: self.RemoveItems(self.List.selectedIndexes()))
        self.MarkAction.triggered.connect(lambda: self.CheckItems(self.List.selectedItems()))

        self.AddButton.pressed.connect(self.AddAction.trigger)
        self.RemoveButton.pressed.connect(self.RemoveAction.trigger)
        self.MarkButton.pressed.connect(self.MarkAction.trigger)
    
    def InitIcons(self):
        self.AddButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_add.png"))
        self.AddAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_add.png"))

        self.RemoveButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_remove.png"))
        self.RemoveAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_remove.png"))

        self.MarkButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/checkbox.png"))
        self.MarkAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/checkbox.png"))

    def AddItem(self):
        item = QListWidgetItem(
            "item",
            parent=self.List,
            type=QListWidgetItem.ItemType.UserType
        )
        item.setCheckState(Qt.CheckState.Unchecked)
        self.List.addItem(item)
    
    def CheckStateBool(self,checkState:Qt.CheckState|int) -> bool:
        return checkState == Qt.CheckState.Checked
    
    def CheckItems (self,items:list[QListWidgetItem]):
        for item in items: item.setCheckState(Qt.CheckState.Unchecked if self.CheckStateBool(item.checkState()) else Qt.CheckState.Checked)
    
    def RemoveItems(self,items:list[QModelIndex]):
        for row in items : self.List.takeItem(row.row())