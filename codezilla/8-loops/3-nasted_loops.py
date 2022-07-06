number_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_list[0][2])
# أول براكيت بيحدد الصف وتاني براكيت بيحدد العمود

for row in number_list:
    print(row)

# كده هيطبعلي كل صف

for row in number_list:
    for column in row:
        print(column)

# كده هيطبعلي كل عنصر
for row in number_list:
    for column in row:
        print(column * 2)

# لو عايز  تعمل عمليه حسابيه يعني
