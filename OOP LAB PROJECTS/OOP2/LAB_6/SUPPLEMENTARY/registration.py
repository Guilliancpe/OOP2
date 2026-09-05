import csv
from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

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
        
        # Makes a label named firstname
        self.Firstname = QLabel("First name: ",self)
        self.Firstname.move(30,45)
        
        # Makes a text field 
        self.Firstname = QLineEdit(self)
        self.Firstname.move(150, 45)
        self.Firstname.resize(100,20)
        self.Firstname.setText(" ")
        
        #Makes a label named Last name 
        self.Lastname = QLabel("Last name: ", self)
        self.Lastname.move(30, 75)
        
        #Makes a text field
        self.Lastname = QLineEdit(self)
        self.Lastname.move(150, 75)
        self.Lastname.resize(100,20)
        self.Lastname.setText(" ")
        
        # Makes a label named Username
        self.Username = QLabel("username: ", self)
        self.Username.move(30, 105)
        
        # Makes a text field
        self.Username = QLineEdit(self)
        self.Username.move(150, 105)
        self.Username.resize(100,20)
        self.Username.setText(" ")
        
        # Makes a label for password
        self.Password = QLabel("password: ", self)
        self.Password.move(30,135)
        
        # Makes a text field
        self.Password = QLineEdit(self)
        self.Password.move(150, 135)
        self.Password.resize(100,20)
        self.Password.setText(" ")
        
        # Makes a label for Email
        self.Email = QLabel("E-mail: ", self)
        self.Email.move(30, 165)
        
        #Text field for email
        self.Email = QLineEdit(self)
        self.Email.move(150, 165)
        self.Email.resize(100,20)
        self.Email.setText(" ")

        # Label for contact
        self.Contact = QLabel("Contact Number: ", self)
        self.Contact.move(30,195)
        
        #Text field for contact
        self.Contact = QLineEdit(self)
        self.Contact.move(150, 195)
        self.Contact.resize(100,20)
        self.Contact.setText(" ")
        
        # In GUI Python, these buttons, textboxes, labels are called Widgets
        # Submit button that registers the accounf
        self.Submit = QPushButton('Submit', self)
        self.Submit.setToolTip("This button register your account")
        self.Submit.move(30,225) # button.move(x,y)
        self.Submit.clicked.connect(self.Account_registration) # Connected to the submit function

        # Clear button that clears the field inputs
        self.Clear = QPushButton('Clear', self)
        self.Clear.setToolTip("This button removes all your inputs")
        self.Clear.move(175,225)
        self.Clear.clicked.connect(self.clear_inputs) #Connected to the clear function
        
        self.show()

    @pyqtSlot()
    def Account_registration(self):
        # I will use .text() to convert the input into a string
        # And I will use .strip() to remove whitespaces inside the string
        inputs = [ self.Firstname.text().strip(),
                  self.Lastname.text().strip(),
                  self.Username.text().strip(),
                  self.Password.text().strip(),
                  self.Email.text().strip(),
                  self.Contact.text().strip()
                ]
        
        # Check if there are empty fields
        for value in inputs:
            if value == "":
                QMessageBox.warning(self, "Missing data", "Please fill in all the fields.", QMessageBox.StandardButton.Ok)
                return
            
        
        
        #Save to a csv file
        with open("Accounts.csv", "a", newline="") as Accounts:
            writer = csv.writer(Accounts)
            writer.writerow(inputs)
            
        #Show that the registration is successful
        QMessageBox.information(self, "Registration", "Registration is successful", QMessageBox.StandardButton.Ok)
        
    # Function for clearing inputs
    # .clear() clears the input 
    @pyqtSlot()
    def clear_inputs(self):
        self.Firstname.clear()
        self.Lastname.clear()
        self.Username.clear()
        self.Password.clear()
        self.Email.clear()
        self.Contact.clear()
