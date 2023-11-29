from pets import Dog
from pets import Cat
from pets import Python

from random import choice

# FROM: https://realpython.com/python-class-constructor/#object-creation-with-__new__

class PetFactory:
    """factory of pets"""
    def __new__(cls):
        ch = choice([Dog, Cat, Python])
        instance = super().__new__(ch)
        print(f"new {type(instance).__name__} exists!")
        return instance

    def __init__(self):
        print("Never runs!")

Pet = PetFactory

class SingletonPet(Pet):
    """singleton of Pet"""    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Pet()
        return cls._instance

myIrrepetiblePet = SingletonPet


