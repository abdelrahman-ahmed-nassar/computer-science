workers_file = open("My_file.text", "r")

print(workers_file.readable())
# بتطلعلي قيمه تقلي هل الملف قابل للقراءه ولا لا

print(workers_file.read())

# بيقرأ الملف كله

print(workers_file.readline())

# بيقرأ السطر وكمان بيحط الكورسر علي السطر اللي بعده فلو كتبتها تاني هتديك السطر الي بعده

print(workers_file.readlines())

# بيحولي كل سطر لقيمه فليست ويطبعلي الليست كلها
# وبتتطبع فشكل ليست برده
# لو عايز سطر محدد
# زي ما بتعمل فالليست بالظبط
print(workers_file.readlines()[1])


# ممكن أعمل

for worker in workers_file.readlines():
    print(worker + "is cool ")

# كده هيطبعلي كل سطر فالملف فالتيرمينال فسطر لوحده
workers_file.close()
