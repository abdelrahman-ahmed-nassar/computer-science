# إنت عايز تعمل فئه من البيانات إسمها موظف لها عدة خصائص وفانكشنز تقدر تعمل منها أشايئ أوبجكتس بعدين 




class Employee:
  def __init__(self, name, age, department, is_manager, rating, salary):
    self.name = name
    self.age = age
    self.department = department
    self.is_manager = is_manager
    self.rating = rating # rating is from 1-5
    self.salary = salary


  def is_excellent(self):
      if self.rating >= 4.5:
        return True 
      else:
        return False


  def bonus(self):
    if self.age == 60:
      self.salary += 500
      print("salary increased to " +str(self.salary))
    else:
      print("no bonus added  your salary is still " +str(self.salary))  



