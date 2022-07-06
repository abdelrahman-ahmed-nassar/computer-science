value = int(input("entrer a number: "))

print(value)

# # دلوقتي لو المستخدم دخل حروف  البرنامج هيضرب
try:
    val = int(input("enter a number: "))
    print(val)
except:
    print("invalid input")

# # كده أنا محددتش نوع الخطأ اللي الإكسبت بتتعامل معاه
# # عشون أكون إحترافي أكتر لازم أحدد نوع الخطأ

try:
    result = 10/0
    valu = int(input("enter a number"))
    print(valu)
except ZeroDivisionError:
    print("you can not devide by zero")
# # كده أنا حددتله المشكله اللي هيتعامل معاها

try:
    int = int(input("enter a number"))
    print(int)
    result = 10/0
except ZeroDivisionError:
    print("you can not devide by zero")

# كده هيعالج مشكله واحده اللي هيا أنا حددتها ولكن لو المستخدم دخل حروف  البرنامج هيبوظ

# بس أنا أقدر أقفش أكتر من إيرور
try:
    integer = int(input("enter a number"))
    print(integer)
    result = 10/0
except ZeroDivisionError:
    print("you can not devide by zero")
except:
    #     # اللي من غير شرط ديه لازم تيجي فالآخر خالص وإسمها ديفولت إكسبت
    print("invalid input")


try:
    num = int(input("enter a number"))
    print(num)
    result = 10/0
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)
# كده إنت تبخزن إسم الإيرور ففاليو
print("success")
