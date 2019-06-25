import time
import random
import string


def get_words_from_file():
    """ Get words from text file """

    file_name = "hangman_words.text"
    with open(file_name, "r") as file:
        words = file.read().split(",")

    return words


def take_guess_from_user():
    """ Take character input from player """

    while True:
        player_input = input("Guess a letter: ")
        if len(player_input) == 1 and player_input in string.ascii_letters:
            break
        print('Please enter only one character')
    return player_input.lower()


def get_random_word_from_words(words, used):
    """ Get a random word from list of words which is not already guessed/used """

    if len(words) == len(used):
        used = []
    while True:
        word = random.choice(words).lower()
        if word not in used:
            break
    return word


def hangman_game(word, number_of_guesses):
    """
    Get guess from player, if guess is present in word then continue else print Wrong letter until player
    won the game or ran out of number of guesses.
    """
    guessed_letters = set()

    print("Start guessing the letter in word..")
    while number_of_guesses > 0:
        failed_guess = False
        for letter in word:
            if letter == " ":
                print(" ", end=" ")
            # check if letter present in guessed_letters
            elif letter in guessed_letters:
                print(letter, sep=" ", end=" ")
            else:
                # Print '_' if letter is not guessed yet
                print("_", sep=" ", end=" ")
                failed_guess = True

        print("")
        # If all letters are guessed in word, print player won
        if not failed_guess:
            print("Congratulations!!! You won")
            break

        print("")
        # Check if user has entered letter which is already guessed
        while True:
            guess = take_guess_from_user()
            if guess not in guessed_letters:
                break
            print(f"{guess} letter is already guessed: {guessed_letters}, please choose different letter")

        # Add guess to guessed letter
        guessed_letters.add(guess)
        if guess not in word:
            print("Wrong letter!!!")
            # Reduce number of guesses on wrong letter attempt
            number_of_guesses -= 1

        print(f"Number of guesses remaining: {number_of_guesses}")

        # Game over if no guesses are remained
        if number_of_guesses == 0:
            print("Game over!!! You loose...")


# Number of guesses allowed for player to guess the word
number_of_guesses_allowed = 10

# List of words from file
all_words = get_words_from_file()
# Set of words that are already used for guessing
used_words = set()

# Get players name
player_name = input("Enter your name: ")

# Welcome player for game
print(f"Welcome {player_name}, Lets start Hangman game(Guess the word)")
time.sleep(1)

while True:
    # Get random word without repeat
    word_in_lower = get_random_word_from_words(all_words, used_words)

    # Add word to used words
    used_words.add(word_in_lower)

    # Play the game
    hangman_game(word=word_in_lower, number_of_guesses=number_of_guesses_allowed)

    """ Get input from player to check if user want to continue playing the game or not """
    continue_input = input("Do you want to continue? Type 'yes' to continue...")
    if continue_input.lower() != 'yes':
        print("Thanks for playing...")
        break

