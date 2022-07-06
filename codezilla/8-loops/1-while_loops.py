# iteration  loops
# reapets the same procedure multipe times until it reaches a specified end point
# بيخليني أعيد كود عدد من المرات من غير ما أضطر أكتب الكود أكتر من مره

i = 1
while i <= 10:
    print(i)
    i += 1
    # or i = i + 1
else:
    print("the condition is not true")
    # اللي جوه الإلس بيحصل مره وحده ومش بيتكرر


print("the loop has ended")

# I refer to iterator
# المحرر بيمشي عالكود سطر سطر
# infinite loop
# bug that can occur when the ending condition is omitted or specified incorrectly

# while i == True:
# print(i)
# i += 1

# continue
# أول ما المحرر بيوصلها بيعدي لفه ومش بيقرأ اللي بعدها وهيرجع للوب من الأول تاني

while i <= 10:
    i += 1
    if i == 6:
        continue
    print(i)

# break
# أول ما المحرر يوصل عندها والشرط بتاعها متحق بيخرج من اللوب خالص

while i <= 10:
    i += 1
    if i == 6:
        break
    print(i)
