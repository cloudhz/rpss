import sys
import random

VALID_CHOICES = set(['rock', 'paper', 'scissors', 'lizard', 'spock'])
WINNER_LOOKUPS = {
    'rock': {
        'win' : ['scissors', 'lizard'],
        'lose' : ['paper', 'spock']
    },
    'paper' : {
        'win' : ['rock', 'spock'],
        'lose': ['scissors', 'lizard']
    },
    'scissors' : {
        'win': ['paper', 'lizard'],
        'lose': ['spock', 'rock']
    },
    'lizard' : {
        'win': ['spock', 'paper'],
        'lose': ['scissors', 'rock']
    },
    'spock' : {
        'win' : ['rock', 'scissors'],
        'lose' : ['lizard', 'paper']
    }
}
SCORE = {
    'win' : 0,
    'lose': 0,
    'tie': 0
}

def update_score(result):
    SCORE[result] += 1

def random_choice():
    return random.sample(VALID_CHOICES, 1)[0]

def pick_winner(user_choice, random_choice):
    if random_choice in WINNER_LOOKUPS[user_choice]['win']:
        update_score('win')
        return 'You win!'
    elif random_choice in WINNER_LOOKUPS[user_choice]['lose']:
        update_score('lose')
        return 'The computer wins!'
    else:
        update_score('tie')
        return 'Draw!'

def main():
    while True:
        try:
            cmd_input = raw_input('Rock, Paper, Scissors, Lizard, Spock! What do you choose? ').lower()
            if cmd_input in VALID_CHOICES:
                print "You chose...", cmd_input
                cpu_input = random_choice()
                print "The computer chose...", cpu_input 
                print pick_winner(cmd_input, cpu_input)
            else:
                print "Please choose a valid move."
        except KeyboardInterrupt:
            print '\n'
            print 'Wins: ', SCORE['win'], 'Losses: ', SCORE['lose'], 'Ties: ', SCORE['tie']
            break

if __name__  == '__main__':
    main()
