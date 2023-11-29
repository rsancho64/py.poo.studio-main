class a:

    def __init__(self):
        self.genA = "A"

    def getGen(self):
        return self.genA


class b:

    def __init__(self):
        self.genB = "B"

    def getGen(self):
        return self.genB


class ab(a, b):

    def __init__(self):
        self.genAB = "ab"

    def getGen(self):
        return self.genAB + a().getGen() + b().getGen()



if __name__ == "__main__":

    a0 = a()
    print(a0.getGen())

    b0 = b()    
    print(b0.getGen())

    ab0 = ab()
    print(ab0.getGen())    

