import copy

# READ: https://stackoverflow.com/questions/1241148/copy-constructor-in-python


class listaCopiable:

    def __init__(self, data):
        self._data = data

    @classmethod
    def from_listaCopiable(cls, lC_original):
        """construccion de copia"""
        data = copy.deepcopy(lC_original._data) # if deepcopy is necessary
        return cls(data)
        
    def __str__(self):
        return f"LC: data: {type(self._data)}: {self._data.__str__()}"

A = [11, [22], [[33]], [[[44]]]]
# print(A)

lc1 = listaCopiable(A)
print(lc1)

lc2 = listaCopiable(lc1)
print(lc1)

# lc1._data.append("innerNew")
# lc1._data[3].append("innerNew")
# lc1._data[3][0].append("innerNew")
lc1._data[3][0][0].append("innerNew")
print(lc1)
print(lc2)  # ANIDAMIENTO???
