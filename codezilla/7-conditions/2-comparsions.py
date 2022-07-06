# ادوات المقارنه بتخلي أقارن بين أي متغيرين أو ليست وبعدين أتخذ قرار بناء علي ناتج المقارنه ديه

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(1, 2, 3))

# أنا كده عملت داله بتاخد 3 أرقام وبتطلعلي أكبر رقم فيهم

print(max(5, 6, 9))
# ديه حاجه جاهزه من بايثون لو عايز


# لو عايز أقران بين إتنين إسترنج

def match_string(str1, str2):
    if str1 == str2:
        print("the strings do match")
    else:
        print("the strings do not match")


match_string("body", "body")
