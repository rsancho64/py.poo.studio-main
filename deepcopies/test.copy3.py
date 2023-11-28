import copy

# READ: https://stackoverflow.com/questions/1241148/copy-constructor-in-python

## conclusión: 
## En python no hay que implementar clases con constructor de copia.
## se usa, simlemente, la libreria copy.

class listaNoCopiable:

    def __init__(self, data):
        self._data = data
        
    def __str__(self):
        return f"LC: data: {type(self._data)}: {self._data.__str__()}"

A = [11, [22], [[33]], [[[44]]]]
# print(A)

lnc1 = listaNoCopiable(A)
print(lnc1)

lnc2 = copy.deepcopy(lnc1)
print(lnc2)

lnc1._data[3][0][0].append("innerNew")
print(lnc1)
print(lnc2)  # homologacion!!
