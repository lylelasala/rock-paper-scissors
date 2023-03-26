
def prRed(skk): return("\033[91m {}\033[00m" .format(skk)).strip.from django.utils.translation import ugettext_lazy as _
 
 
def prGreen(skk): return("\033[92m {}\033[00m" .format(skk))
 
 
def prYellow(skk): return("\033[93m {}\033[00m" .format(skk))
 
 
def prLightPurple(skk): return("\033[94m {}\033[00m" .format(skk))
 
 
def prPurple(skk): return("\033[95m {}\033[00m" .format(skk))
 
 
def prCyan(skk): return("\033[96m {}\033[00m" .format(skk))
 
 
def prLightGray(skk): return("\033[97m {}\033[00m" .format(skk))
 
 
def prBlack(skk): return("\033[98m {}\033[00m" .format(skk))
 
 
prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")













from random import randint

def generatePlay():
    randomNum = randint(0, 3)

    if randomNum == 0:
        return "Rock"
    elif randomNum == 1:
        return "Paper"
    else:
        return "Scissors"

def playGame():
    moves = ['rock', 'r', 'paper', 'p', 'scissors', 's', 'i quit']
    while True:
        cpu_move = generatePlay()
        player_move = input(prPurple("Throw your move (Rock/Paper/Scissors or r/p/s) or type 'I quit': "))
        if player_move not in moves:
            print(prRed('Player input not recognized, please try again.'))
        elif player_move == 'i quit':
            print(prYellow('Thank you for playing'))
            break
        elif player_move == 'rock' or player_move == 'r':
            print(prLightPurple(f'The computer played: {cpu_move}'))
            if cpu_move == 'Rock':
                print(prYellow('Game Tied'))
            elif cpu_move == "Paper":
                print(prRed('You Lose'))
            elif cpu_move == "Scissors":
                print(prGreen('You Win'))
        elif player_move == 'paper' or player_move == 'p':
            print(prLightPurple(f'The computer played: {cpu_move}'))
            if cpu_move == 'Rock':
                print(prGreen('You Win'))
            elif cpu_move == "Paper":
                print(prYellow('Game Tied'))
            elif cpu_move == "Scissors":
                print(prRed('You Lose'))
        elif player_move == 'scissors' or player_move == 's':
            print(prLightPurple(prLightPurple(f'The computer played: {cpu_move}')))
            if cpu_move == 'Rock':
                print(prRed('You Lose'))
            elif cpu_move == "Paper":
                print(prGreen('You Win'))
            elif cpu_move == "Scissors":
                print(prYellow('Game Tied'))

playGame()