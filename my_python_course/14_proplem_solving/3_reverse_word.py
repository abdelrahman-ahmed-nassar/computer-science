word = input("enter the word: ")

list_word = []

for i in range(1, len(word) + 1):
    list_word.append(word[-i])

print("".join(list_word))


