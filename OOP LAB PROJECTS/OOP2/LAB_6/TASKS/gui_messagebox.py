import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):
    
    def __init__(self):
        super().__init__() #Initializes the main window
        #window = QMainWindow()
        self.title = "PyQt Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height) 
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        #In GUI python these buttons and textboxes are called widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100,70) #Move the button's position
        self.button.clicked.connect(self.clickMe)
        
        self.show() # For showing the UI 
        
    @pyqtSlot()
    def clickMe(self):
        # Creating a message box with question "Do you like pyqt6"
        # the name of the window is "Testing response" 
        # and there will be buttons that are "Yes" and "No"
        buttonReply = QMessageBox.question(self, "Testing Response", "Do you like PyQt6?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes) 
        if buttonReply == QMessageBox.StandardButton.Yes:
            QMessageBox.warning(self, "Evaluation", "User clicked: Yes", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            
        else:
            QMessageBox.information(self, "Evaluation", "User clicked: No", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())