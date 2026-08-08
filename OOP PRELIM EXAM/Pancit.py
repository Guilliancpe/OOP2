from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Pancit(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- PANCIT -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 7 and row[7] != "":
                    print("-", row[7])
                                       
    def insert_Pancit(self, ingredient):
        self.insert_ingredient(ingredient, 7)
                    
    def delete_Pancit(self, ingredient):
        self.delete_ingredient(ingredient, 7)
            
pancit = Pancit()
pancit.insert_Pancit("Rice Noodles")
pancit.insert_Pancit("Pork")
pancit.insert_Pancit("Chicken")
pancit.insert_Pancit("Shrimp")
pancit.insert_Pancit("Carrots")
pancit.insert_Pancit("Cabbage")
pancit.insert_Pancit("Green Beans")
pancit.insert_Pancit("Onion")
pancit.insert_Pancit("Garlic")
pancit.insert_Pancit("Soy Sauce")
pancit.insert_Pancit("Fish Sauce")
pancit.insert_Pancit("Black Pepper")