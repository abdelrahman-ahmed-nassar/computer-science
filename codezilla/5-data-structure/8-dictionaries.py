# ممكن يبقا إسمها hashe table فلغات تانيه 
# زي الليست بس بدل ما كل فاليوا لها ترتيب لا ده له مفتاح أو تاج أو تعريف
# keys have values 

convert_month = {
    "Jan": "january",
    "Feb": "february",
    "Mar": "march",
    4: " april",
    "May": 5,
}
# لازم كل مفتاح (تاج )  يكون مختلف عن الباقي وميتككرش
# وينفع أرقام وسترينج وأي حاجه

print(convert_month["Feb"])

# طريقة تانيه
print(convert_month.get("ali", "the value is not exist"))

# مميزتها إني ممكن أعمل رساله عشان لو المستخدم حط باراميتر مش موجود

rolodex = {
  "arron": 5556069,
  "bill": 5559824,
  "jim": 555547,
  "verne": 555309
}
print(rolodex["verne"])

hash("verne")
# بيديلي الرقم المميز اللي الكمبيوتر بيخزن فيه القيمه بس إحنا مبنشفهاش 

# إضافة عناصر للديكشنري 
rolodex["amanda"] = 555974
# كده أنا ضفت عنصر جديد 

rolodex["amanda"] = 55999
# كده غيرت قيمة العنصر 

rolodex["david"] = (5555, 59595)

# ممكن اخزن قيمة فتوبل 
# دلوقتي لو انا معايا الرقم وعايز أعرف الإسم فلازم أعمل 
# reverse 

def caller_id(lookup_number):
  for name, num in rolodex.items():
    if num == lookup_number:
      return name 

print(caller_id(5556069))

# كده أكتبالرقم والإسم يطلعلي
#_____________________________
# associative array : collection o key-value pairs 
# key : value 

# Hash boards 
# keys must be unique 
# values doesn't need to be unique 

# hashing 
# هي عملية تحويل الكلمات إلي كود 

# ASCII
# numercial representation of text characters 
# # t = 116 
# # w = 119 
# 
# 
# collision 
# anytime two inputs produce the same hash vlue
# when two keys have the same hash value
# 
# hash table is an implementation of the associative array abstract data structure 
# . We use the term bucket to describe each entry or place for a key-value pair to go in a hash table. 
#  bucket  = key + value
# 
# 
#  



