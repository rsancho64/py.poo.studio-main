class aSuperClass:
    pass
    
class Employee(aSuperClass):

    # class variables
    company_name = 'NASA'

    # "default" constructor to merely instantiate -wout init data- the object
    # SEE https://realpython.com/python-class-constructor/#object-creation-with-__new__
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        # Customize instance now ...
        cls.salary = 0
        return instance

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # __str__ method
    def __str__(self):
        """vs .show()"""
        return f"Employee: {self.name}, {self.salary}, working @ {self.company_name}"

    # instance method
    def show(self):
        """vs __str__"""
        print('Employee:', self.name, self.salary, "working @", self.company_name)

    def __del__(self):
        print(f"adios mundo cruel")

    # class method
    @classmethod
    def modify_company_name(cls, newName):
        # modify class variable
        cls.company_name = newName    
    
    # TODO: static method: # SEE https://pynative.com/python-static-method/
    @staticmethod
    def sm():
        pass
    
if __name__ == "__main__":

    emp0 = Employee
    print(emp0)

    print()
    
    # emp1 = Employee("Harry", 12000)
    # emp2 = Employee("Emma", 10000)
    # print(emp1)
    # print(emp2)

    # print()

    # emp2.company_name = "SPACEX"
    # print(emp1)
    # print(emp2)

    # print()

    # Employee.modify_company_name("Roscosmos")
    # print(emp1)
    # print(emp2)

    # print()

    # emp3 = Employee("Vasili", 1000)    
    # print(emp1)
    # print(emp2)
    # print(emp3)

    # del emp3
    # print(emp3)