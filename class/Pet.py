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
        print(f"I'm a {type(instance).__name__}!")
        return instance

    def __init__(self):
        print("Never runs!")

