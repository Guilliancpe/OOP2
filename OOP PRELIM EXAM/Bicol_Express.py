from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Bicol_Express(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 5 and row[5] != "":
                    print("-", row[1:])
                                       
    def insert_BC(self, ingredient):
        self.insert_ingredient(ingredient, 5)
                    
    def delete_BC(self, ingredient):
        self.delete_ingredient(ingredient, 5)
            
BC = Bicol_Express()

BC.insert_BC("Pork")
        