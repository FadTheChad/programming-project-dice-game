import random

player1 = { }
player2 = { }


# LOGIN
def login(player):
    player['name'] = input('What is your username')
    player['password'] = input('Enter your password')


# roll dice
def roll():
    dice = random.randint(1, 6)

    return dice


# The Actual Game
def game(player1, player2):
    player1['score'] = 0
    player2['score'] = 0

    for i in range(5):
        print(f'\n\nROUND {i + 1}\n==========\n')

        dice1 = roll()
        dice2 = roll()
        dice = dice1 + dice2

        player1['score'] += dice

        print(player1['name'] + ' scored ' + str(dice1) + ' + ' + str(dice2) + ' = ' + str(dice) + '!')

        dice1 = roll()
        dice2 = roll()
        dice = dice1 + dice2

        player2['score'] += dice

        print(player2['name'] + ' scored ' + str(dice1) + ' + ' + str(dice2) + ' = ' + str(dice) + '!')


def tie_breaker(player1, player2):
    player1['tie_breaker'] = 0
    player2['tie_breaker'] = 0

    while True:
        print('TIED | STARTING TIE BREAKER\n===============')

        dice = roll()
        player1['tie_breaker'] = dice
        print(player1['name'] + ' scored ' + str(dice) + '!')

        dice = roll()
        player2['tie_breaker'] = dice
        print(player2['name'] + ' scored ' + str(dice) + '!')

        if player1['tie_breaker'] != player2['tie_breaker']:
            return


def check_winner(player1_score, player2_score):
    if player1_score > player2_score:
        return '1'

    if player2_score > player1_score:
        return '2'

    return 'tie'

def end_game(winner, opponent, tie_breaker):
    w_score = str(winner['score'])
    o_score = str(opponent['score'])

    print("RESULT\n========")
    if not tie_breaker:
        print(winner['name'] + ' won with ' + w_score + ' points')
        print(winner['name'] + ' | ' + w_score)
        print(opponent['name'] + ' | ' + o_score)
    else:
        w_tb = str(winner['tie_breaker'])
        o_tb = str(opponent['tie_breaker'])

        print(winner['name'] + ' won in the tie breaker with ' + w_tb + ' points')
        print(winner['name'] + ' | ' + w_score + ' | ' + w_tb)
        print(opponent['name'] + ' | ' + o_score + ' | ' + o_tb)

def main():
    login(player1)
    login(player2)

    game(player1, player2)

    winner = check_winner(player1['score'], player2['score'])

    if winner != 'tie':
        if winner == '1':
            end_game(player1, player2, False)
        else:
            end_game(player2, player1, False)
    else:
        tie_breaker(player1, player2)
        winner = check_winner(player1['tie_breaker'], player2['tie_breaker'])

        if winner == '1':
            end_game(player1, player2, True)
        else:
            end_game(player2, player1, True)

main()
