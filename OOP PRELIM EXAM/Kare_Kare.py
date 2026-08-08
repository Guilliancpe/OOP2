from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Kare_Kare(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 6 and row[6] != "":
                    print("-", row[1:])
                                       
    def insert_KK(self, ingredient):
        self.insert_ingredient(ingredient, 6)
                    
    def delete_KK(self, ingredient):
        self.delete_ingredient(ingredient, 6)
            
