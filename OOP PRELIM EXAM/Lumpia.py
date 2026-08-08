from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Lumpia(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 1 and row[1] != "":
                    print("-", row[1:])
                            
        def insert_lumpia(self, ingredient):
            self.insert_ingredient(ingredient, 1)
                    
        def delete_lumpia(self, ingredient):
            self.delete_ingredient(ingredient, 1)
            
lumpia = Lumpia()

lumpia.insert
        