from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Nilaga(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- NILAGA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 3 and row[3] != "":
                    print("-", row[3])
                                       
    def insert_nilaga(self, ingredient):
        self.insert_ingredient(ingredient, 3)
                    
    def delete_nilaga(self, ingredient):
        self.delete_ingredient(ingredient, 3)
            
nilaga = Nilaga()
nilaga.insert_nilaga("Beef")
nilaga.insert_nilaga("Water")
nilaga.insert_nilaga("Potatoes")
nilaga.insert_nilaga("Corn")
nilaga.insert_nilaga("Cabbage")
nilaga.insert_nilaga("Pechay")
nilaga.insert_nilaga("Onion")
nilaga.insert_nilaga("Pepper")
nilaga.insert_nilaga("Fish Sauce")