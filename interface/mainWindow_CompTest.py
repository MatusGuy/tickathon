import sys
sys.path.insert(1,".")
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow as mw

class MW_CompTest():
    ui = mw

    def main(self,window:QMainWindow,app:QApplication):
        print("Main window component test: start")
        self.ui = mw(window,app)
        window.show()
        app.exec_()
        print("Main window component test: complete")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))