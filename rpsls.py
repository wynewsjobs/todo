'''
Created on Oct 19, 2012

@author: Lucas
'''
import random

options =['rock', 'spock', 'paper', 'lizard', 'scissor']

def rpsls(guess):
    result = random.randrange(0, 4)
    print 'computer: '+ options[result]
    guess_index = options.index(guess)
    if result==guess_index:
        return 'tie'
    return who_win(guess_index, result)
    
def who_win(guess_index, result):
    if guess_index-result>0:
        if guess_index-result>2:
            return 'computer win'
        return 'player win'
    else:
        if guess_index + 5 - result>2:
            return 'computer win'
        return 'player win'

            
def play_rpsls(guess):
    print 'player: ' + guess
    print rpsls(guess)

play_rpsls("rock")
    