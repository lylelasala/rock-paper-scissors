from random import randint

def generatePlay():
    randomNum = randint(0, 3)

    if randomNum == 0:
        return "Rock"
    elif randomNum == 1:
        return "Paper"
    else:
        return "Scissors"

def choosePlayer(player_name, playersDict, score = 0, combo = 0, max_combo = 0):
    playersDict.update({player_name: {'score': score, 'combo': combo, 'max_combo': max_combo}})
    return playersDict

def determineRank(score):
    rank = 'Newbie'
    if score == 0:
        return rank
    elif 0 < score <= 5:
        rank = 'Bronze'
    elif 5 < score <= 10:
        rank = 'Silver'
    elif 10 < score <= 15:
        rank = 'Gold'
    elif 15 < score <= 20:
        rank = 'Platinum'
    elif 20 < score <= 25:
        rank = 'Diamond'
    elif 25 < score <= 30:
        rank = 'Master'
    elif 30 < score <= 35:
        rank = 'Grandmaster'
    elif score > 35:
        rank = 'G O A T'
    elif 0 > score >= -5:
        rank = 'Egg'
    elif -5 > score >= -10:
        rank = 'Unlucky'
    elif -10 > score >= -15:
        rank = 'Loser'
    elif -15 > score >= -20:
        rank = 'Weenie'
    elif -20 > score >= -25:
        rank = 'Super Weenie'
    elif -25 > score >= -30:
        rank = 'Mega Weenie Loser'
    elif -30 > score >= -35:
        rank = 'Hardstuck Loser'
    elif score < -35:
        rank = 'Trash'
    return rank
        

def playGame():
    moves = ['rock', 'r', 'paper', 'p', 'scissors', 's', 'rank', 'score', 'create', 'switch', 'i quit', 'players']
    players = {}
    user_name = input("What is your name? ")
    players = choosePlayer(user_name, players)
    score = 0
    combo = 0
    max_combo = 0
    print(f'\nWelcome Player {user_name}!')
    rank = determineRank(0)
    print(f'Looks like your rank is: {rank}, with a score of {score}')
    while True:
        cpu_move = generatePlay()
        player_move = input("\nThrow your move (Rock/Paper/Scissors or r/p/s), 'rank/score', 'create', 'switch', or type 'I quit': ").strip().lower()
        if player_move not in moves:
            print('Player input not recognized, please try again.')
        elif player_move == 'players':
            print(players)
        elif player_move == 'create':
            players = choosePlayer(user_name, players, score, combo, max_combo)
            print('You chose to create a new player\n')
            user_name = input("What is your name? ")
            print(f'\nWelcome Player {user_name}!')
            print(f'Looks like your rank is: Newbie, with a score of {0}')
            players = choosePlayer(user_name, players, 0, 0, 0)
        elif player_move == 'switch':
            while True:
              if len(players) > 1:
                  print('Switching to another player\n')
              else:
                  print('There are no other users to switch to.')
                  break
              players = choosePlayer(user_name, players, score, combo, max_combo)
              user_name = input("Player name you wish to switch to? ")
              if user_name not in players.keys():
                  print(f'Player {user_name} was not found as a player. Try again.\n')
              else:
                  print(f'Switching over to Player "{user_name}"!\n')
                  players = choosePlayer(user_name, players, players[user_name]['score'], players[user_name]['combo'], players[user_name]['max_combo'])
                  print(f'\nWelcome back Player {user_name}!')
                  rank = determineRank(players[user_name]['score'])
                  print(f"\n{user_name}'s rank is: {rank}, with a score of {players[user_name]['score']}")
                  break
        elif player_move == 'rank' or player_move == 'score':
            rank = determineRank(players[user_name]['score'])
            print(f"\n{user_name}'s rank is: {rank}, with a score of {players[user_name]['score']}")
        elif player_move == 'i quit':
            print('Thank you for playing')
            print('[ -- DAILY HIGHSCORES -- ]')
            place = 1
            for player, item in sorted(players.items()):
                print(f"{place}. {player} ---------- Score: {item['score']}, Max Combo: {item['max_combo']} Rank: {determineRank(item['score'])}")
                place += 1
            break
        elif player_move == 'rock' or player_move == 'r':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                print('Game Tied')
            elif cpu_move == "Paper":
                if combo > 1: print('** COMBO BREAK **')
                combo = 0
                score -= 5
                players = choosePlayer(user_name, players, score, combo, max_combo)
                print('You Lose')
            elif cpu_move == "Scissors":
                combo += 1
                if combo > 1 : print(f'COMBO BONUS ==> +{combo}')
                if combo > max_combo: max_combo = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, max_combo)
                print('You Win')
        elif player_move == 'paper' or player_move == 'p':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                combo += 1
                if combo > 1 : print(f'COMBO BONUS ==> +{combo}')
                if combo > max_combo: max_combo = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, max_combo)
                print('You Win')
            elif cpu_move == "Paper":
                print('Game Tied')
            elif cpu_move == "Scissors":
                if combo > 1: print('** COMBO BREAK **')
                combo = 0
                score -= 5
                players = choosePlayer(user_name, players, score, combo, max_combo)
                print('You Lose')
        elif player_move == 'scissors' or player_move == 's':
            print(f'The computer played: {cpu_move}')
            if cpu_move == 'Rock':
                if combo > 1: print('** COMBO BREAK **')
                combo = 0
                score -= 5
                players = choosePlayer(user_name, players, score, combo, max_combo)
                print('You Lose')
            elif cpu_move == "Paper":
                combo += 1
                if combo > 1 : print(f'COMBO BONUS ==> +{combo}')
                if combo > max_combo: max_combo = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, max_combo)
                print('You Win')
            elif cpu_move == "Scissors":
                print('Game Tied')

playGame()