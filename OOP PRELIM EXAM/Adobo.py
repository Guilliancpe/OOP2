import Abstraction, csv
import Insert_Ingredient

class Adobo(Abstraction):
    def show_recipe(self):
        print ("----- ADOBO -----")
        print ("Recipe: ")
        
        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > 0 and row[0] != "":
                    print("-", row[0])
                
    def insert_adobo(self, ingredient):
        self.insert