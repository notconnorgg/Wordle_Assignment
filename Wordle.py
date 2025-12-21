import random

class Colours:
    correct = "\033[32m"
    end ='\033[0m'


# opens a text file in read only mode, and checks to make sure that they are 5 letters long and is in the latin alphabet
def load_words(filename):
    with open(filename, "r") as file:
        return [
            word.strip().lower()
            for word in file
            if len(word.strip()) == 5 and word.strip().isalpha()
        ]

# assigns the defenition load_words to the variable words
words = load_words("words.txt")


def wordle():
    #picks a random words from the word bank
    return random.choice(words)

def letter_hint(guess, wordle_word):
    hint = [""] * 5
    word_list = list(wordle_word)

    #pass 1: Greens (letters in correct position)
    for letter in range(5):
        if guess[letter] == wordle_word[letter]:
            hint[letter] = f"\033[32m{guess[letter]}\033[0m"
            word_list[letter] = None

    #pass 2: yellow/greys (yellow: letters are correct but in the wrong position. grey: letter is incorrect)
    for letter in range(5):
        if hint[letter] != "":
            continue
        if guess[letter] in word_list:
               hint[letter] = f"\033[33m{guess[letter]}\033[0m"
               word_list[word_list.index(guess[letter])] = None
        else:
            hint[letter] = f"\033[90m{guess[letter]}\033[0m"

    return "".join(hint)

def play_game():
    wordle_word = wordle()
    #sets the guess number to 0 when line is run
    guess_number = 0

    # while the user is under 5 gueses this code will run
    while guess_number < 5:
        #asks the user to input a 5-letter word
        user_guess=input("Guess a five letter word:").lower()
        # checks if the users guess is a  5-letter word

        if len(user_guess) != 5:
            print("Please enter exactly five letters")
            continue

        #checks if the users guess is in the word bank
        if user_guess not in words:
            print("Please enter an english word")
            continue

        # checks if the guess is the same as the wordle
        if user_guess == wordle_word:
            print(Colours.correct + user_guess + Colours.end)
            print("Correct!")
            print("you got it in ", guess_number+1 , " guesses!")
            return

        else:
            #displays how many letters where correct.
            print(letter_hint(user_guess, wordle_word))
            #increases the users guess count
            guess_number += 1
            #shows the user how many guesses they have made
            print("current guess: ", guess_number)

        # if user runs out of guesses it will tell the user the wordle
        if guess_number == 5:
            print("the word was:", wordle_word)

#sets the variable play to "true"
play = True
# allows the player to play again without having to restart the program
while play:
    play_game()
    #asks plater if they wish to play again
    play_again=input("Do you want to play again? (y/n)").lower()
    #if player answers no then it the game thanks them for playing and ends the program
    if play_again = "n":
        print('thanks for playing')
        play = False

# allows me to call the word without running wordle() again
wordle_word = wordle()
