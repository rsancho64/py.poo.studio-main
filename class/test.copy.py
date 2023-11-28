import copy

# READ: https://stackoverflow.com/questions/1241148/copy-constructor-in-python

class listaCopiable:

    def __init__(self, algo):
        """implementa construccion de copia"""
        if type(algo) == type(listaCopiable):
            # self.data = copy.deepcopy(algo.data)
            self = copy.deepcopy(algo)
        else:
            self.data = algo

    def __str__(self):
        return f"LC: data: {type(self.data)}: {self.data.__str__()}"

A = [11,[22],[[33]],[[[44]]]]
#print(A)

lc1 = listaCopiable(A)
print(lc1)

lc2 = listaCopiable(lc1)
print(lc1)

# lc1.data.append("innerNew")
# lc1.data[3].append("innerNew")
# lc1.data[3][0].append("innerNew")
lc1.data[3][0][0].append("innerNew")
print(lc1)
print(lc2)  ### ANIDAMIENTO???

