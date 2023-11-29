class contexto:

    def procedimiento(self,unTipo):
        instance = unTipo.__new__(unTipo)
        return instance

c = contexto()
algo = c.procedimiento(float)
print(type(algo))
print(isinstance(algo, float))