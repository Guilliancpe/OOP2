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
    while True:
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
        print("11. Show Ingredients")
        print("12. Exit")
        print("=====================")

        choice = None
        choice = int(input("Input choice: "))
        
        if choice == 12:
            print("Exiting...")
            break
        
        
        
        elif choice == 1:
            
            while True:
                
                if choice == 1:
                    print("====== ADOBO ======")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input choice: "))
                    if new_choice == 1:
                        x = input("Input Ingredient: ")
                        adobo.insert_adobo(x)
                    elif new_choice == 2:
                        x = input("Delete Ingredient: ")
                        adobo.delete_adobo(x)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")              
        elif choice == 2:
            while True:
                    print("===== LUMPIA =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Incput choice: "))
                    if new_choice == 1:
                        y = input("Input Ingredient: ")
                        lumpia.insert_lumpia(y)
                    elif new_choice == 2:
                        y = input("Delete Ingredient: ")
                        lumpia.delete_lumpia(y)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")
        elif choice == 3:
            while True:
                    print("===== SINIGANG =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        z = input("Input Ingredient: ")
                        sinigang.insert_Sinigang(z)
                    elif new_choice == 2:
                        z = input("Delete Ingredient: ")
                        sinigang.delete_Sinigang(z)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")    
                            
        elif choice == 4:
            while True:
                    print("===== NILAGA =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        a = input("Input Ingredient: ")
                        nilaga.insert_nilaga(a)
                    elif new_choice == 2:
                        a = input("Delete Ingredient: ")
                        nilaga.delete_nilaga(a)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid choice!")
                    
        elif choice == 5:
            while True:
                    print("====== BICOL EXPRESS =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        b = input("Input Ingredient: ")
                        BC.insert_BC(b)     
                    elif new_choice == 2:
                        b = input("Delete Ingredient: ")
                        BC.delete_BC(b)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")
                        
        elif choice == 6:
            while True:
                    print("===== SISIG =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input choice: "))
                    if new_choice == 1:
                        c = input("Input Ingredient: ")
                        sisig.insert_Sisig(c)
                    elif new_choice == 2:
                        c = input("Delete Ingredient: ")
                        sisig.delete_Sisig(c)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid choice!")
                    
        elif choice == 7:
            while True:
                    print("===== KARE-KARE ======")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        d = input("Input Ingredient: ")
                        KK.insert_KK(d)
                    elif new_choice == 2:
                        d = input("Delete Ingredient: ")
                        KK.delete_KK(d)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")
                    
        elif choice == 8:
            while True:
                    print("===== PANCIT =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        e = input("Input Ingredient: ")
                        pancit.insert_Pancit(e)
                    elif new_choice == 2:
                        e = input("Delete Item: ")
                        pancit.delete_Pancit(e)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")
                    
        elif choice == 9:
            while True:
                    print("===== CHOPSEUY =====")
                    print("1. New Ingredient")
                    print("2. Delete Item")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        f = input("Input Ingredient: ")
                        chopseuy.insert_Chopseuy(f)
                    elif new_choice == 2:
                        f = input("Delete Ingredient: ")
                        chopseuy.delete_Chopseuy(f)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")
                    
        elif choice == 10:
            while True:
                    print("===== TINOLA =====")
                    print("1. New Ingredient")
                    print("2. Delete Ingredient")
                    print("3. Exit")
                    new_choice = None
                    new_choice = int(input("Input Choice: "))
                    if new_choice == 1:
                        g = input("Input Ingredient: ")              
                        tinola.insert_Tinola(g)
                    elif new_choice == 2:
                        g = input("Delete Ingredient: ")
                        tinola.delete_Tinola(g)
                    elif new_choice == 3:
                        break
                    else:
                        print("Invalid Choice!")  
                
            
MAIN_DRIVER()
        

            
            
        