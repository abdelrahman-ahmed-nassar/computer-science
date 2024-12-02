


secret_word = "carrot"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess2 != secret_word and out_of_guesses == False:
    if guess_count < guess_limit:
        guess2 = input("enter a guess")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print('you lose out of guesses')
else:
    print("you win")
