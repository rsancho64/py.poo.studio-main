import copy

class listaCopiable:

    def __init__(self, algo):
        if type(algo) == type(listaCopiable):
            self.data = copy.deepcopy(algo.data)
        else:
            self.data = algo

    def __str__(self):
        return self.data.__str__()

A = [11,[22],[[33]],[[[44]]]]
print(A)

lc1 = listaCopiable(A)
print(lc1)

lc2 = listaCopiable(lc1)
print(lc1)



# C = copy.copy(A)
# DC = copy.deepcopy(A)

# print(A)
# print(C)
# print(DC)

# id(A)
# id(C)
# id(DC)

# del C
# print(A)
# print(DC)



