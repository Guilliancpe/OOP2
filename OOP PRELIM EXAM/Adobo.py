from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv

#Inheritance
class Adobo(Recipe, InsertnDelete):
    def show_recipe(self):
        print ("----- ADOBO -----")
        print ("Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 0 and row[0] != "":
                    print("-", row[0])
                
    def insert_adobo(self, ingredient):
        self.insert_ingredient(ingredient, 0)
        
    def delete_adobo(self, ingredient):
        self.delete_ingredient(ingredient, 0)
        


        