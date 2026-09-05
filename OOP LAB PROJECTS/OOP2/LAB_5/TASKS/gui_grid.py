import sys
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit,QPushButton, QApplication
from PyQt6.QtGui  import QIcon

class App(QWidget):
    
    # This function sets the position and size of the GUI window
    # and InitUI calls the function InitUI
    def __init__(self):
        super().__init__()
        self.title= "PyQt Login Screen"
        self.x = 200 # Position of the UI in your screen at the x-axis
        self.y = 200 #Position of the UI in your screen at the y-axis
        self.width = 300 # Sets the width of the window
        self.height = 300 # sets the height of the window
        self.InitUI() # Calls the next function
        
    # This function sets up and shows the window  
    def InitUI(self):
        self.setWindowTitle(self.title) # Sets the window title bar
        self.setGeometry(self.x, self.y, self.width, self.height) #defines the window's position and size
        self.setWindowIcon(QIcon('pythonico.ico')) # Applies an Icon for the window
        
        self.createGridLayout() # Calls the next function createGridLayout
        self.setLayout(self.layout) # Applies the layout
        self.show()# Shows the window
        
    # This function creates and arranges the widgets    
    def createGridLayout(self):
        self.layout = QGridLayout() # This creates the layout
        
        self.textboxlbl = QLabel("Text:", self) # Adds a textbox in the window
        self.textbox = QLineEdit(self)

        self.passwordlbl = QLabel("Password:", self) 
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)# Echomode masks the password input

        self.button = QPushButton('Register', self)# Making of a button 
        self.button.setToolTip("You've hovered over me!")

        # Calls the position of each widget
        self.layout.addWidget(self.textboxlbl, 0, 1)
        self.layout.addWidget(self.textbox, 0, 2)
        self.layout.addWidget(self.passwordlbl, 1, 1)
        self.layout.addWidget(self.password, 1, 2)
        self.layout.addWidget(self.button, 2, 2)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())