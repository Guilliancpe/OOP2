import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui  import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainwindow()
        self.title= "Account Registration System"
        self.x=550 # or left
        self.y=250 # or top
        self.width=300
        self.height=280
        self.initUI()
         
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico')) # sets an icon
        
        self.ars = QLabel("Account Registration System", self)
        self.ars.move(70,15)
        
        self.Firstname = QLabel("First name: ",self)
        self.Firstname.move(30,45)
        
        self.Firstname = QLineEdit(self)
        self.Firstname.move(150, 45)
        self.Firstname.resize(100,20)
        self.Firstname.setText(" ")
        
        
        self.Lastname = QLabel("Last name: ", self)
        self.Lastname.move(30, 75)
        
        self.Lastname = QLineEdit(self)
        self.Lastname.move(150, 75)
        self.Lastname.resize(100,20)
        self.Lastname.setText(" ")
        
        self.Username = QLabel("username: ", self)
        self.Username.move(30, 105)
        
        self.Username = QLineEdit(self)
        self.Username.move(150, 105)
        self.Username.resize(100,20)
        self.Username.setText(" ")
        
        self.Password = QLabel("password: ", self)
        self.Password.move(30,135)
        
        self.Password = QLineEdit(self)
        self.Password.move(150, 135)
        self.Password.resize(100,20)
        self.Password.setText(" ")
        
        self.Email = QLabel("E-mail: ", self)
        self.Email.move(30, 165)
        
        self.Email = QLineEdit(self)
        self.Email.move(150, 165)
        self.Email.resize(100,20)
        self.Email.setText(" ")
        
        self.Contact = QLabel("Contact Number: ", self)
        self.Contact.move(30,195)
        
        self.Contact = QLineEdit(self)
        self.Contact.move(150, 195)
        self.Contact.resize(100,20)
        self.Contact.setText(" ")
        
        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.Submit = QPushButton('Submit', self)
        self.Submit.setToolTip("This button does nothing.. yet..")
        self.Submit.move(30,225) # button.move(x,y)


        self.Clear = QPushButton('Clear', self)
        self.Clear.setToolTip("This button does nothing.. yet..")
        self.Clear.move(175,225)
        
        self.show()

