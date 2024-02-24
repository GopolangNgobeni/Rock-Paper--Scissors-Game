import random
import sys
from termcolor import colored

def select_move():
    
    """
    Gets the input move from the player.
    """
    moves = ['r','p','s','q']
    while True:
        player_move = input(colored('\nSelect Move: ','yellow')).lower()
        if player_move == 'q':
            print(colored('Goodbye..', 'light_red'))
            sys.exit()
        elif player_move == '' or player_move not in moves:
            print(colored('Invalid input, Please select (r)ock , (p)aper , (s)cissors , (q)uit','red'))     
        else:
            return moves,player_move


def player_moves(player_move):
    """
    Print the player's chosen move.
    """
    if player_move == 'r':
        print(colored('\nYou chose ROCK','red'))
    elif player_move == 'p':
        print(colored('\nYou chose PAPER','red'))
    elif player_move == 's':
        print(colored('\nYou chose SCISSORS','red')) 
    return player_move        


def computer_moves():
    """
    Generate a random move for the computer.
    """
    computer_move = random.choice(['r', 'p', 's'])
    if computer_move == 'r':
        print(colored('\nVersus ROCK..','blue'))
    elif computer_move == 'p':
        print(colored('\nVersus PAPER..','blue'))
    elif computer_move == 's':
        print(colored('\nVersus SCISSORS','blue'))         
    return computer_move   


def compare_moves(player_move, computer_move,ties, wins, losses):
    """
    Compare the player's and computer's moves and update game statistics.
    """
    if computer_move == player_move:
        print(colored('\nIt\'s a Tie\n','yellow'))
        ties += 1 
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 's' and computer_move == 'p') or \
         (player_move == 'p' and computer_move == 'r'):
         print(colored('\nYou Win..\n','yellow'))
         wins += 1
    elif (computer_move == 'r' and player_move == 's') or \
         (computer_move == 's' and player_move == 'p') or \
         (computer_move == 'p' and player_move == 'r'):
         print(colored('\nComputer wins,You Lose..\n','yellow'))
         losses += 1     
    return ties,wins, losses


def print_game_info(ties,wins,losses):
    """
    Print game information, including rules and current statistics.
    """
    print(colored('ROCK PAPER SCISSOR GAME','magenta'))
    print(colored('Paper covers Rock, Rock crushes Scissors and Scissors cuts Paper','yellow'))
    print(colored('Please select (r)ock , (p)aper , (s)cissors , (q)uit','magenta'))
    print(colored(f'ties: {ties}, wins: {wins}, losses: {losses}','magenta'))
    

def play_again():
    player_input = input(colored('\n\nWould you like to play the Game again?? (Y for Yes and N for No): ','green'))
    if player_input ==  'Y'.lower():
        run_game()
    elif player_input ==  'N'.lower():
        sys.exit()              
    
def run_game():
    """
    Run the Rock, Paper, Scissors game.
    """
    ties = 0
    wins = 0
    losses = 0
    while True:
        print_game_info(ties,wins,losses)
        moves,player_move = select_move()
        player_moves(player_move)
        computer_move = computer_moves()
        ties,wins,losses = compare_moves(player_move, computer_move, ties,wins, losses)
        if wins == 5:
           print(colored(f"Yeey!!! You have {wins} Wins....<<<<<<GAME OVER YOU WIN!!!..>>>>>>>","red"))
           break
        elif losses == 5:
           print(colored(f"Sorry You have {losses} losses... <<<<<<<<<GAME OVER COMPUTER WINS...>>>>>>>>>", "blue"))
           break    
    play_again() 
    
        
if __name__ == '__main__':
      run_game()