class Canonic:
    
    def __init__(self):
        self.value = 11

    def __eq__(self, otro):
        if not isinstance(otro,Canonic):
            return False
        return self.value == otro.value

if __name__ == "__main__":

    canonico0 = Canonic()
    canonico1 = Canonic()
    print(canonico0 == canonico1)
    # print(canonico0.equals(canonico1)) # True

    canonico1.value = 22
    print(canonico0 == canonico1)
    # print(canonico0.equals(canonico1)) # False




