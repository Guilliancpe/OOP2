from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Sisig(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 5 and row[5] != "":
                    print("-", row[1:])
                                       
    def insert_Sisig(self, ingredient):
        self.insert_ingredient(ingredient, 5)
                    
    def delete_Sisig(self, ingredient):
        self.delete_ingredient(ingredient, 5)
            
