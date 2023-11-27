class Employee:

    # class variables
    company_name = 'NASA'

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
    
    # TODO: static method
    def staticmethod():
        pass
    
if __name__ == "__main__":

    # create first object

    # emp0 = new Employee ver como se usa new

    emp1 = Employee("Harry", 12000)
    emp2 = Employee("Emma", 10000)
    print(emp1)
    print(emp2)

    print()

    emp2.company_name = "SPACEX"
    print(emp1)
    print(emp2)

    print()

    Employee.modify_company_name("Roscosmos")
    print(emp1)
    print(emp2)

    print()

    emp3 = Employee("Vasili", 1000)    
    print(emp1)
    print(emp2)
    print(emp3)

    # del emp3
    # print(emp3)