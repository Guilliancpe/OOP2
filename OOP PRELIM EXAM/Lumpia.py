import Abstraction, csv

class Lumpia(Abstraction):
    def show_recipe(self):
        print("----- LUMPIA -----")
        print(" Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
        