def cube(num):
    return num*num*num


print(cube(3))

# the   num    is the parmetar

# the argument  is the number 3

# parameter != Argument
# الفانكشن هديله بارمتر يعمليه عليه شوية عمليات وبعدين الناتج يرجعه
# ويخزن قيمته فالفانكشن

# ممكن أخزن القيمه ففاليو وأرجع أستعملها تاني

result = cube(4)
print(result)
# كده هيطلعلي أربعه اس تلاته


def sum(num1, num2):
    return num1 + num2

# multiple parameter


print(sum(1, 2))
# هيجمع الرقمين


def sub(num1, num2):
    return num1 - num2


print(sum(5, 2))
# هيطرح الرقمين

# أول ما محرر الأكواد بيوصل للسطر اللي في ريتيرن بيسيب الفنكشن ويطلع منه خالص ومبيقرأش إيه اللي بعد كده

# ______________________________
# لاحظ إن الفانكشن الباراميتر هو اللي جوه القوس
# أنما لما نيجي نستدعي الفانكشن ونديله القيمه الأصليه اللي هيشتغل بيها فده إسمه
# argument
# اللي أنا بديله للفانكشن اثناء ال إستدعاء

# لاحظ أن أي فانكشن المتغيرات اللي جواه هي حاجه لوكال وخاصه ببيه وباقي البرنامج مش بيطلع عليها يعني الباراميتر اللي إنت مديله قيمه فالفانكش مينفعش تستعمله فاي حته تانيه

# بمعني إن الفاريابل اللي جوه الفاانكشن ده
# local function
# أنما الفاريبل اللي مكتوب بره الفانكشن ده يبقي عام وممكن أستعمله فالفانكشن برده


# ممكن تحط باريميتير يقبل عدد كبير من الأرجيومنت وهياخدهم ويعملها أكنهم تابل
# tuple
# def test (*the_name_of_parameter):
# print("any thing ")

# test(ali, omar, osaama)


# how to make a function can take any number of the argument by adding them in tuple

def any_number_of_parameter(*par):
    print(par[1])


any_number_of_parameter(1, 2, 3, 4, 6, 78, 78)
