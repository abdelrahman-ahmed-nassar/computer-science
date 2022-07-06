# body languange
# any word have vowel my transelator will convert it to the letter z

def translate(str):
    translation = ""
    for letter in str:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"
        else:
            translation = translation + letter
    return translation


print(translate(input("enter a phrase:  ")))
''' 
ggg

ديه ملاحظه بطريقه غير محبذه 
'''