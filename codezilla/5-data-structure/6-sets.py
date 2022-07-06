# unorded collection of unique items 
college = set(["bill", "katy", "verne","dillon","burce","olivia","richard","jim"])

coworker = set(["aron", "bill", "brandon", "david", "frank","connie", "kyle", "olivia"])

family = set(["garry","landon", "larry", "mark", "olivia","katy", "rea", "tom"])

friends = college.union(coworker, family)

# كده جمعتهم مع بعض وكده كده مفيش ترتيب والأصدقاء المشتركين مش هيتكرروا


# مثال تاني 


""" Sorting Friends into Sets """

# set of all friends
friends = set(['Mark', 'Rae', 'Verne', 'Richard',
              'Aaron', 'David', 'Bruce', 'Garry',
              'Bill', 'Connie', 'Larry', 'Jim',
              'Landon', 'Dillon', 'Frank', 'Tom',
              'Kyle', 'Katy', 'Olivia', 'Brandon'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
                'Rudolph', 'Bill', 'Olivia', 'Jim',
                'Lindsay', 'Rae', 'Mark', 'Kramer',
                'Landon', 'Newman', 'George'])

# set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])


local = friends.intersection(zipcode)

# دلوقتي لوكال هيا الناس المشتركه بين أصدقائي والناس اللي لها نفس الزيب كود بتاعي 
# يعني الفانكشن ديه بتجيب المشترك بين المجموعتين أو التقاطع 

invite = local.difference(munchkins)
munchkins.difference(local)
# الللي بحطه فالأول أنا بشيل منه القيم اللي مشتركه مع المجموعه التانيه اللي جوه القوس وأرجع الباقي اللي فضل فالمجموعه الأولي 
# عشان كده الموضوع بيختلف بين السطرين اللي فاتو 

invite2 = friends.symmetric_difference(olivia)

# ده بيطلع المجال المشترك ويكتب الي فاضل من المجموعتين 
#ومبيفرقش فيها الترتيب

# إضافة عناصر 

"verne" in invite 
# بتلطلعك بوليين فاليو حول هل العنصر ده فالسيت ولا لا 

nvite.add("ss")

invite.remove("ss")

invite.pop()

# بيشيل قيمه عشوائيه من السيت 