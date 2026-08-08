from Abstraction import Recipe
from InsertnDelete import InsertnDelete
import csv


class Kare_Kare(Recipe, InsertnDelete):
    def show_recipe(self):
        print("----- KARE-KARE -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 6 and row[6] != "":
                    print("-", row[6])
                                       
    def insert_KK(self, ingredient):
        self.insert_ingredient(ingredient, 6)
                    
    def delete_KK(self, ingredient):
        self.delete_ingredient(ingredient, 6)
            
KK = Kare_Kare()
KK.insert_KK("Beef")
KK.insert_KK("Peanut Butter")
KK.insert_KK("Peanuts")
KK.insert_KK("Eggplant")
KK.insert_KK("String Beans")
KK.insert_KK("Pechay")
KK.insert_KK("Banana Heart")
KK.insert_KK("Shrimp Paste")
KK.insert_KK("Garlic")
KK.insert_KK("Onion")