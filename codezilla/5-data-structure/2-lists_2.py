programming_languages = ["java", "python", "C++", "C#"]

scripting_languages = ["HTML", "PHP", "javd script"]
#  ممكن تطبع الإتنين مع بعض بس كل ليست لوحده منفصل عن التاني
print(scripting_languages, programming_languages)

# ممكن تدمج إتنين ليست مع بعض وتعملم كونكاتيوناشن
#    .extend()

scripting_languages.extend(programming_languages)
print(scripting_languages)
# أو
programming_languages.extend(scripting_languages)
print(programming_languages)

# أو
scripting_languages += programming_languages
print(scripting_languages)

# أو
scripting_languages = scripting_languages + programming_languages
print(scripting_languages)


# في فنكشن تققدر من خلالها تزود عنصر جديد فآخر اللليست
# .append( )
programming_languages.append("cotlen",)  # ممكن أدمج ليست بدل عنصر عادي
print(programming_languages)

# ماذا لو عايز أزود فأول الليست أو النص
# إستعمل
# .insert()
# بتاخد قيمتين المكان والقيمه
programming_languages.insert(2, "node")
print(programming_languages)


# ممكن تحذف عنصر برده
# .remove()
programming_languages.remove("C++")
print(programming_languages)

# فانكش بتمسح كل حاجه فالليست
# .clear()
# مش بتاخد براميتر
programming_languages.clear()
print(programming_languages)

# في فانكشن بتمسح آخر عنصر فالليست ولا وكمان تقدر تخزن القيمه اللي إتخذفت فمتغير
# .pop()
programming_languages.pop()
# نقدر نخزن القيمه اللي إتحذفت فمتغير
# what_was_poped = scripting_languages.pop()
# print(what_was_poped)
# فهيطلعلنا آخر قيمه فالليست اللي هي إتشالت أصلا

# .index()
# بيعرفني العنصر موجود ولا لا فاللسيت ورقمه وترتيبه كام كمان

print(programming_languages.index("python"))
# تقدر تخزن القيمه اللي هتطلع في متغير

print(programming_languages.count("Css"))
# بيجبلك عدد مرات وجود العنصر فالليست ولو متكرر ولا لا

programming_languages.sort()
print(programming_languages)
# بيعيد ترتيب العناصر اللي جوه الليست أبجديا

list_new = programming_languages.copy
# إنت كده عملت نسخه من الليست ومستقله بنفسها لا تتغير بتغير التانيه
