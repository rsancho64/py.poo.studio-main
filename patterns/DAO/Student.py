class Student:

   def __init__(self, name, rollNo):   # java: Student(String name, int rollNo){
      self.__name = name      # java: this.name = name;
      self.__rollNo = rollNo  # java: this.rollNo = rollNo  

   def getName(self):
      return self.__name 

   def setName(self, name):
      self.__name = name

   def getRollNo(self): 
      return self.__rollNo

   def setRollNo(self, rollNo):
      self.__rollNo = rollNo

if __name__ == "__main__":
   pass
