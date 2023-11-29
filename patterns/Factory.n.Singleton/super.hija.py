class SUPER:

    def __init__(self):
        self.superGen = "11"
        print("i am a SUPER")

    def getGen(self):
        return self.superGen

class HIJA(SUPER):

    def __init__(self):
        self.hijaGen = "22"
        print("i am a HIJA")

    def getGen(self):
        return self.hijaGen + SUPER().getGen()

if __name__ == "__main__":

    S = SUPER()
    print(S.getGen())

    H = HIJA()
    print(H.getGen())





