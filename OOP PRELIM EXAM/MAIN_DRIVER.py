from Adobo import Adobo
from Lumpia import Lumpia
from Sinigang import Sinigang
from Nilaga import Nilaga
from Bicol_Express import Bicol_Express
from Sisig import Sisig
from Kare_Kare import Kare_Kare
from Pancit import Pancit
from Chopseuy import Chopseuy
from Tinola import Tinola


adobo = Adobo()
lumpia = Lumpia()
sinigang = Sinigang()
nilaga = Nilaga()
BC = Bicol_Express()
sisig = Sisig()
KK = Kare_Kare()
pancit = Pancit()
chopseuy = Chopseuy()
tinola = Tinola()



def MAIN_DRIVER():
    
    print("=====RECIPE MENU=====")
    print("1. Adobo")
    print("2. Lumpia")
    print("3. Sinigang")
    print("4. Nilaga")
    print("5. Bicol Express")
    print("6. Sisig")
    print("7. Kare Kare")
    print("8. Pancit")
    print("9. Chopseuy")
    print("10. Tinola")
    print("=====================")

    choice = None
    choice = int(input("Input choice: "))
    
    while choice != -1:
        if choice == 1:
            print("====== ADOBO ======")
            print("1. New Ingredient")
            print("3. Delete Recipe")
            print("4. Exit")
            new_choice = None
            new_choice = int(input("Input choice: "))
            if new_choice == 1:
                x = input("Input Ingredient: ")
                adobo.insert_adobo(x)
            elif new_choice == 2:
                adobo.show_recipe()
            elif new_choice == 3:
                x = input("Delete Ingredient: ")
                adobo.delete_adobo(x)
            elif new_choice == 4:
                return
            
MAIN_DRIVER()
        

            
            
        