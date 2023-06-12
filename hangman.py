# Course: A Practical Introduction to Python Programming
# Institution: Lancaster University
# Author: María Isabel Sánchez-O'Mullony Martínez
# Date: 31/12/2022

from hangmanClass import hangman # Import hangman stored in hangmanClass.py

game = hangman(username="Nikoleta")
game.startGame()

# ~~~~~~~~~~~different examples~~~~~~~~~~
# Even if you specify the word length, if you specify the word this word length won't be taken into account

# hangman(username="Isabel", wordLength = 8).startGame()
# hangman(username="Isabel", word = 'hello').startGame()
# hangman(username="Isabel", wordLength = 8, word = 'hello').startGame()
