# ملهاش علاقه بإسمها سيبك من إنها معناها  "ل"  بس الموضوع مختلف
# هي حاجه بديها متغير وبعد المتغير الحاجه اللي عايز أعمل عليها معالجه
# أفضل ترجمه ليها هي إنك تسميها الحلقه التكراريه إنك عايز تعمل فانكشن يتكرر أكتر من مره
for letter in "codezilla":
    print(letter)
# هيطبعلي كل حرف من الكلمه بمعني إنه راح عالحرف الأول وطبعه ورجع تاني طبع اللي بعديه لحد ما الكلمه خلصت  وكل حرف مطبوع فسطر لوحده
'''
for :
specifies a variabe name thet we can use in each iteration of the loop to reference the current value 

in :
indicate thet what follows is the set of values that we want to iterate through 

iteration
Reapets the same procedure multiple times until it reaches a specefic endpoint

loop
code that iterates, moving from beginning to end of the process, then starting over


iteration
1- specify the data
2- what should happen to the data
3- what is the end point


'''

buddies = ["ali", "ahmed", "osama", "omar"]

for buddy in buddies:
    print(buddy)

# كده هيطبعلي كل إسم جوه الليست
# بمعني هيعدي علي كل قيمه قيمه هياخدها هيخزنها فالمتغير اللي إنت حاطه وبعدين يعمل عليه معالجه ولما يخلص يخش عالمتغير اللي بعده

for x in range(10):
    print(x)
# كده هيبدأ من 0 ل 10 يعني مش هيطبع العشره لأن العد فلبرمجه بيبدأ من عشره فهو هياخد الصفر ويعمله معالجه ويطبعه وبعدين يخش عالي بعده
for y in range(5, 10):
    print(y)
#  كده هيطبع من أول خمسه لحد رقم 9 ومش هيطبع 10

for z in range(len(buddies)):
    print(z)

# len(buddies )# بدل ما أقعد أعد عدد العناصر اللي جوه الليست فكده أكني بالظبط شلت
# وحطيت 4
for index in range(3):
    print(buddies[index])

for num in range(10):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
# هيعدي علي عدد عدد من أول صفر لحد عشره ويشوفهولي لو هو بيحقق الشرط ولما يخلص بيخرج

for some_one in range(len(buddies)):
    if buddies[some_one] == "ali":
        print(some_one, "is the winner")
    else:
        print(some_one, "is not the winner")

for friend in buddies:
    if friend == "omar":
        print(friend, " is your friend")
        break
else:
    print(" not found")
# البريك معناها إن أول ما يتحقق الشرط إخرج من اللوب
# والإلس معروفه

# continue
# بتتخطي لفه واحده

for t in range(3, 10):
    if t == 5:
        continue
    print(t, " is the chosen number")
