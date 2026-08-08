from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Sinigang(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- SINIGANG -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 2 and row[2] != "":
                    print("-", row[2])
                                       
    def insert_Sinigang(self, ingredient):
        self.insert_ingredient(ingredient, 2)
                    
    def delete_Sinigang(self, ingredient):
        self.delete_ingredient(ingredient, 2)
            

        