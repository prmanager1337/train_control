# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from Widget_switch import *
# =============================================================================

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Testing UI")
        #self.resize(800, 480)
        width = 800
        height = 480

        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.centralWidget = windowLayout(self)
        self.setCentralWidget(self.centralWidget)
        self.createMenuBar()

    def createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())