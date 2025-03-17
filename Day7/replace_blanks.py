import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)
chosen_word_list = list(chosen_word)
#todo Create a placeholder with the same number of blanks as the chosen_word
guess = input("Guess a letter: \n").lower()

placeholder = ""
for i in chosen_word:
    placeholder+= "_"


#todo create a display that puts the guess letter in the right space
display = ""

for letter in chosen_word_list:
    if guess == letter:
        display += letter
    else:
        display += "_"

print(display)