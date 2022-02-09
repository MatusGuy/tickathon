from sys import path as sp
sp.insert(1,'.')

from PyQt5.QtWidgets import QListWidgetItem,QMainWindow,QApplication, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QObject, Qt, QModelIndex, QDateTime, QMimeData

from interface.mainUi import Ui_MainWindow as ui
from components.prefMng import PreferencesManager

from dist import pydist as pd

def DestroyQObject(object:QObject):
    object.setParent(None)
    object.deleteLater()

class ListWidgetItem(QListWidgetItem,QObject):
    item = QListWidgetItem
    object = QObject

    def __init__(self,text,parent,type):
        self.InitItem(text,parent,type)
        self.InitObject(parent)

    def InitItem(self,text,parent,type):
        self.item = QListWidgetItem(text,parent,type)
        return self.item
    def InitObject(self,parent):
        self.object = QObject(parent)
        return self.object

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication
    prefMng = PreferencesManager("items.json")

    items = []

    def __init__(self,window:QMainWindow,app:QApplication):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")

        super().__init__()
        super().setupUi(self.window)
        self.InitIcons()
        self.InitListContextMenu()
        self.DisableItemCreationTimeLabel()

        self.AddAction.triggered.connect(self.AddItem)
        self.RemoveAction.triggered.connect(lambda: self.RemoveItems(self.List.selectedIndexes()))
        self.MarkAction.triggered.connect(lambda: self.CheckItems(self.List.selectedItems()))
        self.ClearAction.triggered.connect(self.List.clear)

        self.AddButton.pressed.connect(self.AddAction.trigger)
        self.RemoveButton.pressed.connect(self.RemoveAction.trigger)
        self.MarkButton.pressed.connect(self.MarkAction.trigger)
        self.ClearButton.pressed.connect(self.ClearAction.trigger)

        self.List.itemSelectionChanged.connect(lambda: self.UpdateItemInfo(self.List.selectedIndexes()))
    
    def InitListContextMenu(self):
        self.List.customContextMenuRequested.connect(lambda: self.ListMenu.exec_(QCursor.pos()))
    
    def InitIcons(self):
        self.AddButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_add.png"))
        self.AddAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_add.png"))

        self.RemoveButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_remove.png"))
        self.RemoveAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/edit_remove.png"))

        self.MarkButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/checkbox.png"))
        self.MarkAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/checkbox.png"))

        self.ClearButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/logout.png"))
        self.ClearAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/logout.png"))

        self.window.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+"assets/tickathon.png"))
    
    def DisableItemCreationTimeLabel(self):
        self.ItemCreationTime.setDisabled(True)
    def EnableItemCreationTimeLabel(self,date:QDateTime):
        self.ItemCreationTime.setDateTime(date)
        self.ItemCreationTime.setEnabled(True)
    
    def ClearSelection(self):
        for sItem in self.List.selectedItems(): sItem.setSelected(False)
    
    def UpdateItemInfo(self,selectedItems:list[QModelIndex]):
        self.SelectedCount.setValue(len(selectedItems))

        if len(selectedItems)>=1:
            self.IndexesOutput.setEnabled(True)
            stringIndexes = []
            for index in selectedItems: stringIndexes.append(index.row()+1)
            self.IndexesOutput.setText(str(stringIndexes))
        else:
            self.IndexesOutput.setDisabled(False)

        if len(selectedItems)==1:
            ctime = self.items[selectedItems[0].row()].object.property("CREATION_TIME")
            if ctime == None:
                self.DisableItemCreationTimeLabel()
                return
            
            self.EnableItemCreationTimeLabel(ctime)
        else: self.DisableItemCreationTimeLabel()
    
    def GetItems(self) -> list[QListWidgetItem]: return self.List.items(QMimeData())
    def GetNames(self) -> list[str]:
        resp = []
        for item in self.GetItems():
            name = item.text()
            resp.append(name)
        return resp

    def AddItem(self):
        a = ListWidgetItem(
            text=f"item {self.List.count()+1}",
            parent=self.List,
            type=QListWidgetItem.ItemType.UserType
        )
        self.items.append(a)
        a.item.setCheckState(Qt.CheckState.Unchecked)
        a.item.setFlags(
            Qt.ItemFlag.ItemIsEditable|
            Qt.ItemFlag.ItemIsEnabled|
            Qt.ItemFlag.ItemIsUserCheckable|
            Qt.ItemFlag.ItemIsSelectable|
            Qt.ItemFlag.ItemIsDragEnabled
        )

        self.ClearSelection()
        a.item.setSelected(True)

        a.object.setProperty("CREATION_TIME",QDateTime.currentDateTime())

        self.List.addItem(a.item)
    
    def CheckStateBool(self,checkState:Qt.CheckState|int) -> bool: return checkState == Qt.CheckState.Checked
    
    def CheckItems (self,items:list[QListWidgetItem]):
        for item in items:
            item.setCheckState(Qt.CheckState.Unchecked if self.CheckStateBool(item.checkState()) else Qt.CheckState.Checked)
    
    def RemoveItem(self,row:int):
        self.ClearSelection()
        self.items[row].object.setProperty("CREATION_TIME",None)
        self.items.pop(row)
        self.List.takeItem(row)

    def RemoveItems(self,items:list[QModelIndex]):
        if len(items)>0:
            items.reverse()
            for index in items: self.RemoveItem(index.row())
        else:
            if self.List.count()>0:
                resp,button = QInputDialog.getText(
                    self.window,
                    "Remove item",
                    "Input the item's position to remove the chosen item:\nSeperate the values by commas (,) to remove multiple items"
                )

                try:
                    rows = resp.split(",")
                    for row in rows: rows[rows.index(row)] = int(row)-1
                    rows.sort()
                    rows.reverse()

                    print(rows)

                    for row in rows: self.RemoveItem(row)

                except IndexError as err:
                    self.ErrorDialog("Couldn't find any items with those positions.")

                except ValueError as err:
                    if button==QInputDialog.DialogCode.Accepted:
                        self.ErrorDialog("Those aren't numbers.\nPlease make sure you didn't include any whitespaces.")
            else:
                self.ErrorDialog("List is empty.")
    
    def OnAppQuit(self):
        if pd.__PyDist__._isBundle:
            for item in self.GetItems():
                date = self.items[item].object.property("CREATION_TIME")
                self.prefMng.SetSetting(["items",self.List.indexFromItem(item).row()],
                    {
                        "name": item.text(),
                        "checked": self.CheckStateBool(item.checkState()),
                        "date": {
                            "year": str(date.date().year()),
                            "month": str(date.date().month()),
                            "day": str(date.date().day()),
                            "hour": str(date.time().hour()),
                            "minute": str(date.time().minute()),
                        }
                    }
                )
    
    def ErrorDialog(self,errormsg:str,returnObject:bool=True) -> QMessageBox.StandardButton|int|QMessageBox:
        dialog = QMessageBox(
            QMessageBox.Icon.Critical,
            "Error",
            errormsg,
            QMessageBox.StandardButton.Ok,
            self.window
        )
        dialog.setWindowIcon(self.window.windowIcon())
        resp = None
        if returnObject: resp = dialog.exec_()

        if returnObject: DestroyQObject(dialog)

        return resp if returnObject else dialog