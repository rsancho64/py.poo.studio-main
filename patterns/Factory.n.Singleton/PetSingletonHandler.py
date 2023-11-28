from Pet import *

if __name__ == "__main__":

    pet0 = myIrrepetiblePet()
    pet1 = myIrrepetiblePet()
    pet2 = myIrrepetiblePet()    
    if ((pet0 is pet1) and (pet1 is pet2)):
        print(f"todos son el mismo, solo hay uno")

    pet2.communicate()
