from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Chopseuy(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 8 and row[8] != "":
                    print("-", row[1:])
                                       
    def insert_Chopseuy(self, ingredient):
        self.insert_ingredient(ingredient, 8)
                    
    def delete_Chopseuy(self, ingredient):
        self.delete_ingredient(ingredient, 8)
            
