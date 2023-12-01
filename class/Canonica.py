#! /usr/bin/python3

import json
import copy


class Canonic:

    def __init__(self):
        self.val = {}  # {e1: 11}  # None :/

    def __eq__(self, otro):
        if not isinstance(otro, Canonic):
            return False
        return self.val == otro.val

    def __hash__(self):
        return hash(repr(self))

    def to_json(self):
        return json.dumps(self, default=lambda self: self.__dict__)  # type??

    # str vs str :
    # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/repr/python-repr/
    # (https://www.toppr.com/guides/python-guide/references/methods-and-functions/)

    def __str__(self):
        """user-friendly version; 
        pragma: goal : **readable**
        container’s __str__ **uses** contained objects’ __repr__
        """
        return f"{repr(self.val)}"  # ~ ... self.val.__repr__()

    def __repr__(self):
        """developer-friendly string; 
        pragma: goal : **unambiguous**
        """
        # return f"{type(self)}@{id(self)}::{repr(self.val)}"  ## as repr
        return f"{type(self)}@{id(self)}::{self.to_json()}"  # as json

    def __voidcopy(self):  # solo un uso. suprimir?
        return Canonic()

    def __copy__(self):
        newone = self.__voidcopy()
        newone.val = copy.deepcopy(self.val)
        return newone

    def __canonicformat(self, string):
        return string.lower().strip()

    def put(self, **kv):
        """to grow.n.update"""
        for k, v in kv.items():
            if isinstance(v, str):
                v = self.__canonicformat(v)
            self.val[k] = v

    def pop(self, *keys):
        """to decrease"""
        for k in keys:
            self.val.pop(k, None)

    def __lt__(self, other):
        """ # TODO
        see: https://stackoverflow.com/questions/7152497/making-a-python-user-defined-class-sortable-hashable
        the only method to use sortable ?
        """
        return True  # TODO


if __name__ == "__main__":

    c0 = Canonic()
    print(c0)

    c0.pop("uno", "dos", "tres")  # k's not in data

    c0.put(nombre="ramon")
    c0.put(edad=25)
    c0.put(caracter="guason")
    print(hash(c0), c0)

    c0.pop("caracter")
    print(hash(c0), c0)

    c0.put(caracter="  guAsON ")
    print(hash(c0), c0)

    # cc = []
    # cc.append(Canonic()) # 1st
    # cc.append(Canonic()) # 2nd

    # # list comprehensions: https://python-intermedio.readthedocs.io/es/latest/comprehensions.html
    # # list comprehensions to print:
    # #    https://stackoverflow.com/questions/37084246/printing-using-list-comprehension
    # print( *(c for c in cc))

    # cc[0].write(k1="v1")
    # cc[0].write(k2="v2")
    # print( *(c for c in cc))

    # cc.append(copy.deepcopy(cc[0]))  # 3rd
    # print( *(c for c in cc))

    # print(cc[0] == cc[2])
    # print(cc[0] is cc[2])

    # print( *(id(c) for c in cc))
    # print( *(c.to_json() for c in cc))
    # print( *(repr(c) for c in cc))
