from Pet import *

if __name__ == "__main__":

    pet1 = PetFactory()  # I'm  ...
    pet1.communicate()  # ...

    print(isinstance(pet1, PetFactory))  # FALSE !!
    print(isinstance(pet1, Dog))  # T or F ...

    pet2 = PetFactory()  # I'm  ...
    pet2.communicate()  # ...
