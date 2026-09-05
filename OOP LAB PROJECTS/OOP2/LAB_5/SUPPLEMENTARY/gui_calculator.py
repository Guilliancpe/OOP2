# Grid Layout
import sys
import math
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QPushButton, QWidget, QApplication, QMainWindow, QMessageBox, QMenuBar
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # Calls InitUI to set the window up

    def initUI(self):
        grid = QGridLayout() # Creates the grid layout
        self.setLayout(grid) # Applies the grid layout

        # Menu creation
        Menu = QMenuBar(self)
        
        # Creates the file menu
        filetab = Menu.addMenu("File")
        
        # History option
        newhistory = filetab.addAction("history")
        # For showing the history
        newhistory.triggered.connect(self.showhistory)
        
        #Exit shortcut
        exitact = filetab.addAction("Exit")
        exitact.triggered.connect(self.close)
        #Exit using Ctrl + Q
        exitact.setShortcut("Ctrl+Q")
        
        #add the menubar to the grid
        grid.addWidget(Menu, 0,0,1,5)

        # Button labels arranged in rows
        names = [               
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['^', 'sin', 'cos', 'C']
        ]

        # Text box field at the top and places it onto the grid
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 1, 0, 1, 5)
        
        # using a loop to generate positions
        positions = [(i, j) for i in range(2, 7) for j in range(0, 4)]
        # flatten the list into a singlelist
        newnames = [item for row in names for item in row] 
        #pair each position with a button label
        for position, name in zip(positions, newnames):
            if name == '':
                continue
            button = QPushButton(name) # This is a button creator
            grid.addWidget(button, *position) # This places the button on the grid

            # Creates a tiny function that connects to the button 
            # so I dont have to use more def functions.
            # This returns a text rather than the actual function
            button.clicked.connect(lambda checked, text=name: self.Button(text))
            
        
        self.setGeometry(300, 300, 200, 150) # Sets window size and position
        self.setWindowTitle('Grid Layout') # Sets the window title
        self.show() # shows the window when InitUI is called
        
    # A function for the arithmetic and trigonometry functions  
    def Button(self, text):
        newButton = self.textLine.text()
        

        # for the = button
        # Checkif the button pressed is an equal sign
        if text == '=':
            # Error handling 
            try:
                #Store the original operation
                operation = newButton
                # replace ^ symbol with ** for exponentiation
                newButton = newButton.replace('^', '**')
                #Evaluate the mathematical expression
                result = eval(newButton)
                #Display the result
                self.textLine.setText(str(result))
                #Save the operation and result
                self.savehistory(operation, result)
            except:
                #Print out error if something is wrong
                self.textLine.setText("Error")
                
        # For the sin button   
        elif text == 'sin':
            try:
                #Store the value as a float
                num = float(newButton)
                # Convert from degrees to radians
                result = math.sin(math.radians(num))  
                # Display the result  
                self.textLine.setText(str(result))
                #Save the result
                self.savehistory("sin(" + newButton + ")",result)
            except:
                self.textLine.setText("Error")  
        
        # For the cos button        
        elif text == 'cos':
            try:
                num = float(newButton)
                result = math.cos(math.radians(num))
                self.textLine.setText(str(result))
                self.savehistory("cos(" + newButton + ")", result)
            except:
                self.textLine.setText("Error")   
                        
        else:
            self.textLine.setText(newButton + text)
            
        if text == 'C':
            self.textLine.clear()

    # for showing the history
    def showhistory(self):
        #error handling
        try:
            # Open and read calcfile
            with open("Calc_history.txt", "r") as calcfile:
                history = calcfile.read()
            #If the file is empty display the message    
            if history == "":
                history = "There is nothing here..."
                
        except FileNotFoundError:
            # If the file does not exist display the message
            history = "The file does not exist"
            
        QMessageBox.information(self, "Calculator History", history)
            
    # Save history function
    # Used in the sin, cos, and = operations
    def savehistory(self, operation, result):
        # Open and append the operation and result 
        with open("Calc_history.txt", "a") as calcfile:
            calcfile.write(operation + " = " + str(result) + "\n")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec())

