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
                if len(row) > 4 and row[4] != "":
                    print("-", row[4])
                                       
    def insert_BC(self, ingredient):
        self.insert_ingredient(ingredient, 4)
                    
    def delete_BC(self, ingredient):
        self.delete_ingredient(ingredient, 4)
