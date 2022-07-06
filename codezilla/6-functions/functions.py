# مجموعه من الأكواد مهمهتها إنها تنفذلي مهمه واحده بدل ما أقعد أكرر الحاجه ديه
# defination

def The_name_of_functions():
    print("hello ")
# لاحظ لازم يكون في مسافه قبل المهمه عشان تتضمن ضمن الفنكشن


# عشان تستدعي الفنكشن بتكتب إسمه وبعده أقواس
The_name_of_functions()

# ممكن آخد شوية معلومات وأضمنها فالفنكشن عشان تبقي أحسن


def say_hi(name):
    print("hello " + name)


say_hi("ali")
# parametar اللي بين الأقواس إسمه
# أو ممكن لو عايز إسم المستخدم هو اللي يكتبه

name = input("print your name : ")


def Inputs(name):
    print("hello "+name)


Inputs(name)

# parametar ممكن تدي الفانكشن أكتر من


def parametar(name, age):
    print("hello " + name + " your age is "+str(age))
# لاحظ إن إحنا حولنا الرقم لسترينج عشان نعرف نطبعه مع سترينج فنفس الجمله


parametar("ali", 15)
