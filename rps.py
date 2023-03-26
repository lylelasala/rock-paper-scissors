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
        player_move = input("Throw your move (Rock/Paper/Scissors or r/p/s) or type 'I quit': ").strip().lower()
        if player_move not in moves:
            print('Player input not recognized, please try again.')
        elif player_move == 'i quit':
            print('Thank you for playing')
            break
        elif player_move == 'rock' or player_move == 'r':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                print('Game Tied')
            elif cpu_move == "Paper":
                print('You Lose')
            elif cpu_move == "Scissors":
                print('You Win')
        elif player_move == 'paper' or player_move == 'p':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                print('You Win')
            elif cpu_move == "Paper":
                print('Game Tied')
            elif cpu_move == "Scissors":
                print('You Lose')
        elif player_move == 'scissors' or player_move == 's':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                print('You Lose')
            elif cpu_move == "Paper":
                print('You Win')
            elif cpu_move == "Scissors":
                print('Game Tied')

playGame()