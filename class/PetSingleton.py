# FROM: https://realpython.com/python-class-constructor/#object-creation-with-__new__

class Singleton(Pet):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


first = Singleton()
second = Singleton()
first is second
