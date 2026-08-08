from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Tinola(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- TINOLA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 9 and row[9] != "":
                    print("-", row[9])
                                       
    def insert_Tinola(self, ingredient):
        self.insert_ingredient(ingredient, 9)
                    
    def delete_Tinola(self, ingredient):
        self.delete_ingredient(ingredient, 9)
        
tinola = Tinola()
tinola.insert_Tinola("Chicken")
tinola.insert_Tinola("Ginger")
tinola.insert_Tinola("Garlic")
tinola.insert_Tinola("Onion")
tinola.insert_Tinola("Green Papaya")
tinola.insert_Tinola("Chili Leaves")
tinola.insert_Tinola("Fish Sauce")
tinola.insert_Tinola("Black Pepper")
tinola.insert_Tinola("Water")            
