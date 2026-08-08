import Parentfile as PF
import csv

class Insert(PF):
    def insert_ingredient(self, ingredient, column):
        
        with open(self.filename, "r", newline="") as file:
            rows = list(csv.reader(file))
            
        for row in rows:
            while len(row) <= column:
                row.append("")
            
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
                
                