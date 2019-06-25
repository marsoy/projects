# Hangman Game (Guess the word)

The word to guess is represented by a row of dashes, representing each letter of the word.

The player guessing the word may, at any time, attempt to guess the whole word. If the word is correct, the game is over and the guesser wins. Otherwise,
number of guesses will be reduced. If player is unable to guess the word before there are no guesses
remain, player will loose.  

## Current Version
- Take words form text file to guess
- Word to be guessed selected randomly and without repeat
- Word displayed on terminal with '_'
- Player guess the letter for selected word 
- If player win or ran out of guesses then player prompted to continue. 'Yes' for continue otherwise exit
 
 ## Future Version
 - Words can be categorized to different categories for example Animals, Fruits, Places etc
 - According category words are assigned 
 For example:
 {'animals': ['monkey', 'lion', 'elephant'],
 'places': ['madrid', 'mumbai', 'bangalore']}
 - Category and words both will be selected randomly and hint will be provided according to 
 selected category.
 - Number of guesses allowed can be taken from config file
 - We can add time constraints along with number of guesses
 