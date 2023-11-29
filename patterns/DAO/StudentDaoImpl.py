import Student

class StudentDao:

       # class variables
   _students = {}
	
   def __init__(self):
      # self._students[0] = "Robert"
      # self._students[1] = "John"
      pass

   def deleteStudent(self, rollNo):
      if rollNo in self._students.keys():
         del self._students[rollNo]
         print(f"Student: rollNo: {rollNo} deleted from DB")
      else:
         print(f"Student: rollNo: not in DB")         

   def getStudent(self, rollNo):
      return self._students[rollNo]
   
   def getlistStudent(self):
      return self._students
      
   def updateStudent(self, rollNo, name):
      if not rollNo in self._students.keys():
         mens = f"Student: {rollNo}/{name} appened to BD.. "         
      else:
         mens = f"Student: {rollNo} updated to {name} in BD.. "
      print(mens, end="")
      self._students[rollNo] = name
      print("..done")
      
if __name__ == "__main__":

   sDao = StudentDao()
   print(sDao.getlistStudent())
   
   sDao.updateStudent(0, "Robert")
   sDao.updateStudent(1, "John")
   print(sDao.getlistStudent())
   
   sDao.updateStudent(1, "Martha")   
   print(sDao.getlistStudent())

