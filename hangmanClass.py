import os
import random
import pickle
from string import punctuation

class hangman:

    def __init__(self, username='', wordLength=0, word=''):
        self.username = username
        self.wordLength = wordLength
        self.word = word


    # takes a random word to guess
    def getWord(self):
        if self.word == '':
            word_founded = False
            # we put the words of the file into a list
            with open(os.path.join(os.path.dirname(__file__), "words.txt"), "r") as file:
                words = file.read().split()

            if self.wordLength > 0:
                # to only choose a word that has the length that has been specified
                while word_founded == False:
                    word = words[random.randint(0, len(words)-1)] # get a random word to guess
                    if len(word) == self.wordLength:
                        word_founded = True
            # if the word length hasn't been specified
            else:
                word = words[random.randint(0, len(words)-1)] # get a random word to guess
        else:
            word = self.word.lower()
            temp = list(word) # separate the word in letters
            # check if there is something that is not a letter, if there is ends the program
            for t in temp:
                if t in punctuation or t.isalpha() == False or t == ' ':
                    print("The word that you gave is wrong")
                    exit()
    
        return word


    # displays the state of the hangman
    def displayHangman(self, guesses):
         # put the different states of the game in a list (the drawings), taken from the pickle file
        with open(os.path.join(os.path.dirname(__file__), 'hangmanStates.pkl'), 'rb') as pickle_load:
            hangman = pickle.load(pickle_load) 

        print(hangman[6-guesses]) # prints the actual state of the hangman


    # displays what we have guessed
    def displayWord(self, word, guessed_letters):
        count = 0
        line = ""

        while count < len(word):
            for letter in word:
                # if one letter has been guessed it displays this letter
                if letter in guessed_letters:
                    line += letter
                    count += 1
                # if the letter hasn't been guessed yet it will put it as a "blank space"
                else:
                    line += '_'
                    count += 1

        return line


    def checkGame(self, word, line, letters, guesses):
        count = 0

        # if you don't have more guesses you lose
        if guesses == 0:
            print(f"Ah that sucks, sorry you lost! The word was {word}\n")
            return True

        # if you have guessed all the letters you win
        for letter in line:
            if letter != '_':
                count += 1
        if count == letters:
            print("Congratulations! You have won!")
            return True
        
        return False
            

    def startGame(self):
        guesses = 6 # number of guesses we have
        guessed_letters = []
        incorrect_letters = []
        game = False
        
        # initial state of the game
        word = self.getWord()
        letters = list(word)
        print(f"Hi {self.username}! Your game has been generated and is ready to go!")
        self.displayHangman(guesses)
        print(self.displayWord(letters, guessed_letters))
        print(f"Guesses left: {guesses}!")

        while game == False:
            # starts asking the user to choose a letter
            userInput = input("Please pick a letter that you would like to guess: ")
            # if you already put this letter
            if userInput in guessed_letters:
                    print("You've already guessed that!")
            else:
                # the input must be one letter
                if userInput.isalpha() and len(userInput) == 1:
                    guessed_letters.append(userInput) # adds the letter to the list with the guessed letters

                    # if the letter is not in the word we are guessing
                    if userInput not in word:
                        incorrect_letters.append(userInput) # adds it to the list with the mistakes
                        guesses -= 1 # you have one less guess

                    self.displayHangman(guesses) # displays the drawing

                    # displays what we have of the word
                    line = self.displayWord(letters, guessed_letters) 
                    print(line)

                    print(f"Your incorrect guesses: {incorrect_letters}")
                    print(f"Guesses left: {guesses}!")

                    game = self.checkGame(word, line, len(letters), guesses)
                else:
                    print("Incorrect input")
