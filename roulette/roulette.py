'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
import math
random.seed(1)

class Bet:    
    def __init__(self, name, num_list):
        self.name = name
        self.bet_amt = 0
        self.bet_numbers = num_list
        self.add_bet()

    def add_bet(self):
        money = int(input("How much would you like to bet on {}? ".format(self.name)))
        self.bet_amt = money 
        print("You have betted {} on {}".format(self.bet_amt, self.bet_numbers))

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

board = [1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]

betting_list = {1:"Red",2:"Green",3:"Black", 4:"Straight", 5:"Column", 6:"Even", 7:"Odd", 8:"Dozen(1-3)",
9:"Six line", 10:"Split", 11:"Street", 12:"Corner", 13:"Top-line"}

def roll_ball():
    '''returns a random number between 0 and 37'''
    landed_num = math.floor(random.random() * 38)
    return landed_num

def check_results(ball_pos,total_bets):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    print('..')
    for bet in total_bets:
        print(bet.bet_numbers)
def payout():
    '''returns total amount won or lost by user based on results of roll. '''
def update_bank(amount):
    bank_account -= amount
    
def col_list(col_num):
    arr = []
    for col in board:
        arr.append(col[col_num-1])
    print(arr)


def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    """
    bank_account = 1000
    total_bets = []
    while(bank_account > 0):
        
        print("You currently have ${}".format(bank_account))
        for a, b in betting_list.items():
            print('{} {}'.format(a, b))
        menu_option =int(input("Choose a number,(0 to spin)"))
        if (menu_option == 1):
            bet = Bet(betting_list[menu_option], red)
        elif(menu_option ==2):
            bet = Bet(betting_list[menu_option],green)
        elif(menu_option == 3):
            bet = Bet(betting_list[menu_option],black)
        elif(menu_option == 4):
            bet_number = int(input("Which number would you like to guess"))
            bet = Bet(betting_list[menu_option],bet_number)
        elif(menu_option == 5):
            column = int(input("Which column would you like to choose, 1...3? "))
            bet = Bet(betting_list[menu_option],col_list(column))
        elif(menu_option == 6):
            bet = Bet(betting_list[menu_option], [range(1,37,2)] ) 
        elif(menu_option == 7):
            bet = Bet(betting_list[menu_option], [range(0,37,2)] )
        elif(menu_option == 8):
            dozen_num = int(input("(1) 1-12 (2) 13-24 (3) 25-36"))
            bet = Bet(betting_list[menu_option], range(1,13)+12*(dozen_num-1) )
        elif(menu_option == 9):
            two_cols = int(input("Choose a colum from 1-11 and second will follow"))
            bet = Bet(betting_list[menu_option], board[two_cols]+board[two_cols+1])
        elif(menu_option == 0):
            check_results(roll_ball,total_bets)
            break
            
        total_bets.append(bet)
        bank_account -= bet.bet_amt
play_game()
