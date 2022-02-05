from sys import path as sp
sp.insert(1,'.')

from PyQt5.QtWidgets import QListWidgetItem,QMainWindow,QApplication
from PyQt5.QtCore import QObject, Qt
from interface.mainUi import Ui_MainWindow as ui

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication

    def __init__(self,window:QMainWindow,app:QApplication):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")

        super().__init__()
        super().setupUi(self.window)

        self.AddButton.pressed.connect(self.AddItem)
        self.RemoveButton.pressed.connect(lambda: self.RemoveItems(self.List.selectedIndexes()))
        self.MarkButton.pressed.connect(lambda: self.CheckItems(self.List.selectedItems()))
    
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
    
    def CheckItems(self,items:list[QListWidgetItem]):
        for item in items: item.setCheckState(Qt.CheckState.Unchecked if self.CheckStateBool(item.checkState()) else Qt.CheckState.Checked)
    
    def RemoveItems(self,items:list[QListWidgetItem]):
        for row in items:
            self.List.takeItem(row)