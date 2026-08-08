import os, csv

class Parent_file:
    def __init__(self, filename = "Recipe.csv"):
        self.filename = filename
    
    def create_file(self):
        if not os.path.exists(self.filename):
             with open(self.filename, "a", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow([ "Adobo", "Lumpia", "Sinigang", "Nilaga", 
                                "Bicol Express", "Sisig", "Kare-Kare", " Pancit", 
                                "Chopseuy", "Tinola"])