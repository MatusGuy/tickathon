import sys
sys.path.insert(1,".")
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface.mainWindow import MainWindow as mw

class MW():
    ui = mw

    def main(self,window:QMainWindow,app:QApplication):
        self.ui = mw(window,app)
        window.show()
        app.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW()
    sys.exit(theApp.main(window,app))