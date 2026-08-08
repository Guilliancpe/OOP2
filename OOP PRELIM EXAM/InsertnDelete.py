from Parentfile import Parent_file
import csv

class InsertnDelete(Parent_file):
    def insert_ingredient(self, ingredient, column):
        self.create_file()
        
        with open(self.filename, "r", newline="") as file:
            rows = list(csv.reader(file))
            
        for row in rows:
            while len(row) <= column:
                row.append("")
            
        for row in rows[1:]: #for loop so it checks everything
            if row[column].lower() == ingredient.lower(): 
                print("Ingredient already exists!")
                return
            
        for row in rows[1:]:
            if row[column] == "":
                row[column] = ingredient
                break
                
        else:
            row2 = [""] * len(rows[0])
            row2[column] = ingredient
            rows.append(row2)
            
        with open(self.filename, "w", newline="") as file:
            csv.writer(file).writerows(rows)
    
    def delete_ingredient(self, ingredient, column):

        with open(self.filename, "r", newline="") as file:
            rows = list(csv.reader(file))

        for row in rows[1:]:
            if len(row) > column and row[column].lower() == ingredient.lower():
                row[column] = ""
                break

        with open(self.filename, "w", newline="") as file:
            csv.writer(file).writerows(rows)    
                