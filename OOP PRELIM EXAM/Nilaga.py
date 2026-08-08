from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Nilaga(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 4 and row[4] != "":
                    print("-", row[1:])
                                       
    def insert_nilaga(self, ingredient):
        self.insert_ingredient(ingredient, 4)
                    
    def delete_nilaga(self, ingredient):
        self.delete_ingredient(ingredient, 4)
            
nilaga = Nilaga()

nilaga.insert_nilaga("Beef")
        