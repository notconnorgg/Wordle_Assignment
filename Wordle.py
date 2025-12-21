import random

class Colours:
    correct = "\033[32m"
    end ='\033[0m'

def load_words(filename):
    with open(filename, "r") as file:
        return [
            word.strip().lower()
            for word in file
            if len(word.strip()) == 5 and word.strip().isalpha()
        ]

words = load_words("words.txt")
#words=['house', 'shops', 'warns', 'falls', 'aback', 'fugue', 'actor', 'aware', 'docks','arise','store','sound','clear','round','learn','great','spark','flame','scene','stone']

def wordle():
    #picks a random words from the word bank
    return random.choice(words)

def letter_hint(guess, wordle_word):
    hint = [""] * 5
    word_list = list(wordle_word)

    #pass 1: Greens
    for letter in range(5):
        if guess[letter] == wordle_word[letter]:
            hint[letter] = f"\033[32m{guess[letter]}\033[0m"
            word_list[letter] = None

    #pass 2: yellow/greys
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

    guess_number = 0

    while guess_number < 5:
        #asks the user to input a 5-letter word
        user_guess=input("Guess a five letter word:").lower()
        if len(user_guess) != 5:
            print("Please enter exactly five letters")
            continue
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
            print(letter_hint(user_guess, wordle_word))
            guess_number += 1
            print("current guess: ", guess_number)
        # if user runs out of guesses it will tell the user the wordle
        if guess_number == 5:
            print("the word was:", wordle_word)

# allows the player to play again without having to restart the program
play = True
while play:
    play_game()

    play_again=input("Do you want to play again? (y/n)").lower()
    if play_again != "y":
        print('thanks for playing')
        play = False

# allows me to call the word without running wordle() again
wordle_word = wordle()
