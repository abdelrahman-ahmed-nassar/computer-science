# هنا هعمل كلاس يورث كل الصفات اللي فالأصلي وممكن أزود عليه أو أغير فيه بدل ما أعمل واحد جديد 



from Doctor import doctor

class family_doctor(doctor):
  def what_specialization(self):
    print("i work with families")

  def paid_by_who(self):
    print("I paid by people")