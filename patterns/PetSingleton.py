# FROM: https://realpython.com/python-class-constructor/#object-creation-with-__new__

# a Singleton class with a .__new__() method that 
# allows the creation of only one instance at a time.
# To do this, .__new__() checks the existence of 
# previous instances cached on a class attribute:

from Pet import *

class SingletonPet(Pet):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Pet()
        return cls._instance

myIrrepetiblePet = SingletonPet

