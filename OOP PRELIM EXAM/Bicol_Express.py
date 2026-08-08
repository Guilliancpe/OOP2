from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Bicol_Express(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- BICOL EXPRESS -----")
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

BC = Bicol_Express()
BC.insert_BC("Pork")
BC.insert_BC("Coconut Milk")
BC.insert_BC("Coconut Cream")
BC.insert_BC("Chili Peppers")
BC.insert_BC("Shrimp Paste")
BC.insert_BC("Garlic")
BC.insert_BC("Onion")
BC.insert_BC("Ginger")
BC.insert_BC("Fish Sauce")
BC.insert_BC("Black Pepper")