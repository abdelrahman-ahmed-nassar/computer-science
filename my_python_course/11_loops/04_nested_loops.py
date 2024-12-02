

number_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(number_list[0][2])


# print every row
for row in number_list:
    print(row)


# print every element

for row in number_list:
    for column in row:
        print(column)
