from Abstraction import Recipe
from Insert import Insert
import csv

#Inheritance
class Adobo(Recipe, Insert):
    def show_recipe(self):
        print ("----- ADOBO -----")
        print ("Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 0 and row[0] != "":
                    print("-", row[1:])
                
    def insert_adobo(self, ingredient):
        self.insert_ingredient(ingredient, 0)

#Object creation
adobo = Adobo()

adobo.insert_adobo("Pork")
adobo.show_recipe()
        