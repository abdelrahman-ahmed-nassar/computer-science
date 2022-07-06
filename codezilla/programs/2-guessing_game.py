secret_word = "Body"
guess = ""

while guess != secret_word:
    guess = input("enter a guess")

print("you win")

# هنعقدها شويه بحيث إن المستخدم له عدد محاولات محدد
secret_word2 = "body"
guess2 = " "
guess_count = 0
gues_limit = 3
out_of_guesses = False


while guess2 != secret_word2 and out_of_guesses == False:
    if guess_count < gues_limit:
        guess2 = input("enter a guess")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print('you lose out of guesses')
else:
    print("you win")
