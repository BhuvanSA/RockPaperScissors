import random
import os
import sys

def welcome():
    os.system('clear')
    print("Welcome to Rock Paper Scissors")
    print("Can you win against the Computer?")
    r = int(input('How many rounds do you want to play?\n'))
    print("Okay")
    return r

def playerChoice():
    pc = ''
    while pc  not in choices:
        pc = input('Rock Paper Scissors???\n').strip().lower()
    print()
    print('Player Choice    : ',pc)
    return pc

def computerChoice():
    cc = random.choice(choices)
    print('Computer Choice  : ',cc)
    return cc

def compare(pc,cc):
    global ps,cs,i
    print()
    if (pc == cc):
        return 'Round Draw Repeat'
    elif ((pc == 'rock' and cc == 'paper') or (pc == 'paper' and cc == 'scissors') or (pc == 'scissors' and cc == 'rock')):
        cs+=1
        i+=1
        return 'Computer won the Round'
    else:
        ps+=1
        i+=1
        return 'Player won the Round'

def score():
    print()
    print('Player       : {:^10}'.format(ps))
    print('Computer     : {:^10}'.format(cs))
    print()

def round():
    print(i,': ',compare(playerChoice(),computerChoice()))
    score()

def brain():
    global r,ps,cs,i
    rem = r-i
    if (ps > cs + rem):
        return False
    elif (cs > ps + rem):
        return False
    return True

def whoWon():
    global ps,cs
    if (ps > cs):
        return 'Player Won!!! Congratulations'
    elif (cs > ps):
        return 'Computer Won!!! Hehe'

choices = ['rock','paper','scissors']
cs = ps =  0
i = 1
y = ''
while True:
    r = welcome()
    while brain():
        round()
    print(whoWon())
    cs=ps=pc=cc=r=0
    i = 1
    y = input('Do you want to play again Y/N:\n').lower().strip()
    if y == 'n':
        sys.exit(0)

sys.exit(0)



