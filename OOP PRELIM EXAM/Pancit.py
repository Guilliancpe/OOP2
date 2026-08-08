from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Pancit(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 7 and row[7] != "":
                    print("-", row[1:])
                                       
    def insert_Pancit(self, ingredient):
        self.insert_ingredient(ingredient, 7)
                    
    def delete_Pancit(self, ingredient):
        self.delete_ingredient(ingredient, 7)
            
Pancit = Pancit()

Pancit.insert_Pancit("Noodles")
        