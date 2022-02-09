# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SOFTWARE\PythonProjects\todoList\interface\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/tickathon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setStyleSheet("QPushButton{\n"
"    image: url()\n"
"}\n"
"\n"
"QPushButton#AddButton:hover{\n"
"    background-color: rgb(85, 255, 0)\n"
"}\n"
"QPushButton#RemoveButton:hover{\n"
"    background-color: rgb(252, 78, 78)\n"
"}\n"
"QPushButton#MarkButton:hover{\n"
"    background-color: rgb(59, 168, 255)\n"
"}\n"
"QPushButton#ClearButton:hover{\n"
"    background-color: rgb(255, 101, 0)\n"
"}")
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.AddButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setObjectName("AddButton")
        self.gridLayout.addWidget(self.AddButton, 0, 4, 1, 1)
        self.RemoveButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RemoveButton.setIcon(icon2)
        self.RemoveButton.setObjectName("RemoveButton")
        self.gridLayout.addWidget(self.RemoveButton, 1, 4, 1, 1)
        self.MarkButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MarkButton.sizePolicy().hasHeightForWidth())
        self.MarkButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/checkbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MarkButton.setIcon(icon3)
        self.MarkButton.setObjectName("MarkButton")
        self.gridLayout.addWidget(self.MarkButton, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 4, 2, 1)
        self.ClearButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ClearButton.sizePolicy().hasHeightForWidth())
        self.ClearButton.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon4)
        self.ClearButton.setObjectName("ClearButton")
        self.gridLayout.addWidget(self.ClearButton, 3, 4, 1, 1)
        self.List = QtWidgets.QListWidget(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.List.sizePolicy().hasHeightForWidth())
        self.List.setSizePolicy(sizePolicy)
        self.List.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.List.setDragEnabled(True)
        self.List.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.List.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.List.setAlternatingRowColors(False)
        self.List.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.List.setViewMode(QtWidgets.QListView.ListMode)
        self.List.setModelColumn(0)
        self.List.setWordWrap(True)
        self.List.setObjectName("List")
        self.gridLayout.addWidget(self.List, 0, 0, 6, 4)
        self.widget = QtWidgets.QWidget(self.MainWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SelectedLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectedLabel.sizePolicy().hasHeightForWidth())
        self.SelectedLabel.setSizePolicy(sizePolicy)
        self.SelectedLabel.setObjectName("SelectedLabel")
        self.gridLayout_2.addWidget(self.SelectedLabel, 0, 0, 1, 1)
        self.CreationTimeLabel = QtWidgets.QLabel(self.widget)
        self.CreationTimeLabel.setObjectName("CreationTimeLabel")
        self.gridLayout_2.addWidget(self.CreationTimeLabel, 3, 0, 1, 1)
        self.ItemCreationTime = QtWidgets.QDateTimeEdit(self.widget)
        self.ItemCreationTime.setEnabled(False)
        self.ItemCreationTime.setReadOnly(True)
        self.ItemCreationTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ItemCreationTime.setObjectName("ItemCreationTime")
        self.gridLayout_2.addWidget(self.ItemCreationTime, 3, 1, 1, 2)
        self.SelectedCount = QtWidgets.QSpinBox(self.widget)
        self.SelectedCount.setReadOnly(True)
        self.SelectedCount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.SelectedCount.setObjectName("SelectedCount")
        self.gridLayout_2.addWidget(self.SelectedCount, 0, 1, 1, 2)
        self.hSep1 = QtWidgets.QFrame(self.widget)
        self.hSep1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hSep1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hSep1.setObjectName("hSep1")
        self.gridLayout_2.addWidget(self.hSep1, 1, 0, 1, 3)
        self.IndexesLabel = QtWidgets.QLabel(self.widget)
        self.IndexesLabel.setObjectName("IndexesLabel")
        self.gridLayout_2.addWidget(self.IndexesLabel, 2, 0, 1, 1)
        self.IndexesOutput = QtWidgets.QLineEdit(self.widget)
        self.IndexesOutput.setEnabled(False)
        self.IndexesOutput.setReadOnly(True)
        self.IndexesOutput.setObjectName("IndexesOutput")
        self.gridLayout_2.addWidget(self.IndexesOutput, 2, 1, 1, 2)
        self.gridLayout.addWidget(self.widget, 6, 0, 1, 5)
        MainWindow.setCentralWidget(self.MainWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.MenuBar.setObjectName("MenuBar")
        self.ListMenu = QtWidgets.QMenu(self.MenuBar)
        self.ListMenu.setObjectName("ListMenu")
        self.Help = QtWidgets.QMenu(self.MenuBar)
        self.Help.setObjectName("Help")
        self.View = QtWidgets.QMenu(self.MenuBar)
        self.View.setObjectName("View")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.AddAction = QtWidgets.QAction(MainWindow)
        self.AddAction.setIcon(icon1)
        self.AddAction.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.AddAction.setObjectName("AddAction")
        self.RemoveAction = QtWidgets.QAction(MainWindow)
        self.RemoveAction.setIcon(icon2)
        self.RemoveAction.setObjectName("RemoveAction")
        self.MarkAction = QtWidgets.QAction(MainWindow)
        self.MarkAction.setIcon(icon3)
        self.MarkAction.setObjectName("MarkAction")
        self.ClearAction = QtWidgets.QAction(MainWindow)
        self.ClearAction.setIcon(icon4)
        self.ClearAction.setObjectName("ClearAction")
        self.AboutAction = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutAction.setIcon(icon5)
        self.AboutAction.setObjectName("AboutAction")
        self.ActiveItems = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("e:\\SOFTWARE\\PythonProjects\\todoList\\interface\\../assets/view_text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ActiveItems.setIcon(icon6)
        self.ActiveItems.setObjectName("ActiveItems")
        self.ListMenu.addAction(self.AddAction)
        self.ListMenu.addAction(self.RemoveAction)
        self.ListMenu.addAction(self.MarkAction)
        self.ListMenu.addSeparator()
        self.ListMenu.addAction(self.ClearAction)
        self.Help.addAction(self.AboutAction)
        self.View.addAction(self.ActiveItems)
        self.MenuBar.addAction(self.ListMenu.menuAction())
        self.MenuBar.addAction(self.View.menuAction())
        self.MenuBar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tickathon"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.RemoveButton.setText(_translate("MainWindow", "Remove"))
        self.MarkButton.setText(_translate("MainWindow", "Toggle mark"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.SelectedLabel.setText(_translate("MainWindow", "Selected:"))
        self.CreationTimeLabel.setText(_translate("MainWindow", "Creation time:"))
        self.IndexesLabel.setText(_translate("MainWindow", "Indexes in list:"))
        self.ListMenu.setTitle(_translate("MainWindow", "List"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.View.setTitle(_translate("MainWindow", "View"))
        self.AddAction.setText(_translate("MainWindow", "Add item(s)"))
        self.AddAction.setShortcut(_translate("MainWindow", "Ins"))
        self.RemoveAction.setText(_translate("MainWindow", "Remove item(s)"))
        self.RemoveAction.setShortcut(_translate("MainWindow", "Del, Backspace"))
        self.MarkAction.setText(_translate("MainWindow", "Toggle mark item(s)"))
        self.MarkAction.setToolTip(_translate("MainWindow", "Mark item"))
        self.MarkAction.setShortcut(_translate("MainWindow", "Space"))
        self.ClearAction.setText(_translate("MainWindow", "Clear list"))
        self.ClearAction.setShortcut(_translate("MainWindow", "Shift+Del, Shift+Backspace"))
        self.AboutAction.setText(_translate("MainWindow", "About"))
        self.AboutAction.setShortcut(_translate("MainWindow", "F1"))
        self.ActiveItems.setText(_translate("MainWindow", "Active items"))
        self.ActiveItems.setShortcut(_translate("MainWindow", "Ctrl+Shift+I"))
