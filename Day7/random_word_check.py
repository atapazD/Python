word_list = ["aardvark", "baboon", "camel"]
import random

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word and print it
chosen_word = random.choice(word_list)
print(chosen_word)

# todo-2 ask the user to guess a letter and assign the answer to avariable called guess. Make guess lowercase.
guess = input("Choose a letter:\n").lower()
print (guess)
# todo-3 check if letter that user guess is one of the letters in the chosen word and print right if it is and wrong if its not.

chosen_word_list = list(chosen_word)
print (chosen_word_list)
for letter in chosen_word_list:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")