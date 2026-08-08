from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Sisig(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- SISIG -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 5 and row[5] != "":
                    print("-", row[5])
                                       
    def insert_Sisig(self, ingredient):
        self.insert_ingredient(ingredient, 5)
                    
    def delete_Sisig(self, ingredient):
        self.delete_ingredient(ingredient, 5)
            
sisig = Sisig()
sisig.insert_Sisig("Pork")
sisig.insert_Sisig("Chicken Liver")
sisig.insert_Sisig("Onion")
sisig.insert_Sisig("Chili Peppers")
sisig.insert_Sisig("Calamansi")
sisig.insert_Sisig("Mayonnaise")
sisig.insert_Sisig("Soy Sauce")
sisig.insert_Sisig("Black Pepper")
sisig.insert_Sisig("Salt")