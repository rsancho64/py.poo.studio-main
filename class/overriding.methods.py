class Parent(object):
    """class parent"""
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class Child(Parent):
    """class child"""    
    # pass
    def get_value(self):
        return self.value + 1

if __name__ == "__main__":

    p = Parent()
    c = Child()

    # print(dir(p))
    # print(dir(c))

    # print(dir(Parent))
    # print(dir(Child))

    print(c.get_value()) # 5,6

    print(Parent.__dict__)
    print()
    print(Child.__dict__)
