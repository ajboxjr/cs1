#psuedoCode
'''
Ask the user for their word
get the length of the word and make that many boxes

ask for the user word input or ask if they want to complete the whole word

if 1 word:
	check if (word) contains
	if not:
		add wrong words

function
get_guesses:
	len of the set



'''
import random
import math
import os


# Creating the board for the hangman words
def create_display(hangman_letters):
	game_board = ''
	for letter in hangman_letters:
		if(letter.isspace()):
			game_board += ' '
		elif(letter.isalpha()):
			game_board += '_'
	print(game_board)
	return list(game_board)

def clear_screen():
    os.system('clear')

# use user guess to compare to chars
def update_board(board,guess):
	for index in range(len(secret_word)):
		if(secret_word[index] == guess):
			board[index] = guess
			


# Check to see if the character is in the set of Hangman word
def is_correct(guess_char):
	if(guess_char in set(secret_word)):
		print("{} guess char was there".format(guess_char))
		guessed_chars.append(guess_char)
		return True

	elif(guess_char in set_bad_guesses):
		print("You have already guessed this letter, try again")
		return False

	else:
		set_bad_guesses.add(guess_char)
		return False


# Define hung as having more guesses
def is_hung():
	return gueses_amt < len(set_bad_guesses)


def display(board):
	print('Tries {}/{}'.format(len(set_bad_guesses), gueses_amt))
	for letter in board:
		print(letter, sep='\n ', end='', flush=True)
	


# Create gameloop  for hangman
def gameplay(secret_word):
    clear_screen()
    board = create_display(secret_word)
    while(board != list(secret_word)):
        usr_guess = input("What is your guess letter: ")[0]
        if(is_correct(usr_guess)):
            print(usr_guess+" was a letter in the word")
            update_board(board,usr_guess)
        if(is_hung()):
            print("You lost")
            break
        display(board)
    else:
        print("\n you won!!")


# Create a set of wordsed in The Hangman word.
gueses_amt = 7
set_bad_guesses = set()
board = []
secret_word = ''
guessed_chars = []

if __name__ == '__main__':
	secret_word = input("Welcome to hangman please enter the word ").lower()
	print("that you would like to guess:\t")
	gameplay(secret_word)
