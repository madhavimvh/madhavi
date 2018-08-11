'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s_s = "abcdefghijklmnopqrstuvwxyz"
    l_l = list(s_s)
    for i in letters_guessed:
        if i in l_l:
            l_l.remove(i)
    ss_s = ''.join(l_l)
    return ss_s
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    a = ""
    for i in secret_word:
        if i in letters_guessed:
            a = a+i
        else:
            a = a+" _ "
    return(a)
    

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for i in secret_word:
        if i in letters_guessed:
            secret_word = secret_word.replace(i,"")
    if secret_word == "":
        return True
    return False
def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " +str(len(secret_word)) +" letters long.")
    i = 8
    flag = 0
    letters_guessed = []
    while i >= 1:
        print("you have " + str(i) + "guesses left")
        if i <= 8 and flag == 1:
            print("available letterskhk: " + get_available_letters(letters_guessed))
        if i == 8 and flag == 0:
            print("available letters: " + get_available_letters(letters_guessed))
            flag = 1
        guess = input("guess a letter")
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            else:
                print("oops! you've guessed the answer wrong" + get_guessed_word(secret_word, letters_guessed))
                i -= 1
        else:
            print("you've already used that letter earlier, try an other guess")
        e = is_word_guessed(secret_word, letters_guessed)
        if e:
            return "congratulations, you won!"
        if i == 0 and e == False:
            return "sorry, you ran out of guesses, the word was: " + secret_word
            
    
   
def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
    
    secret_word = chooseWord(wordlist).lower()
    print(hangman(secret_word))
	


if __name__ == "__main__":
    main()
