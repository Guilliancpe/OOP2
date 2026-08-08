from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Tinola(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 10 and row[10] != "":
                    print("-", row[1:])
                                       
    def insert_Tinola(self, ingredient):
        self.insert_ingredient(ingredient, 10)
                    
    def delete_Tinola(self, ingredient):
        self.delete_ingredient(ingredient, 10)
            
Tinola = Tinola()

Tinola.insert_Tinola("Chicken")
        