# Grid Layout
import sys
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QApplication



class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # Calls InitUI to set the window up

    def initUI(self):
        grid = QGridLayout() # Creates the grid layout
        self.setLayout(grid) # Applies the grid layout

        # Button labels arranged in rows
        names = [               
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Text box field at the top and places it onto the grid
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 1, 1, 5)
        
        # using a loop to generate positions
        positions = [(i, j) for i in range(1, 7) for j in range(1, 5)]
        # flatten the list into a singlelist
        newnames = [item for row in names for item in row] 
        #pair each position with a button label
        for position, name in zip(positions, newnames):
            if name == '':
                continue
            button = QPushButton(name) # This is a button creator
            grid.addWidget(button, *position) # This places the button on the grid

        self.setGeometry(300, 300, 200, 150) # Sets window size and position
        self.setWindowTitle('Grid Layout') # Sets the window title
        self.show() # shows the window when InitUI is called

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec())

