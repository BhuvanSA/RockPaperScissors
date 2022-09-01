import random
import os
import time
import sys
ps,cs = 0,0
def compare(pc,cc):
    global ps,cs,turns
    if (pc == cc):
        return 'Round Draw'
    elif ((pc == 'rock' and cc == 'paper') or (pc == 'paper' and cc == 'scissors') or (pc == 'scissors' and cc == 'rock')):
        cs+=1
        turns+=1
        return 'Computer wins'
    else:
        ps+=1
        turns+=1
        return 'Player wins'
def winCheck(rounds):
    rem = turns-rounds
    if  ps+rem > cs+rem:
        return 'person' 
    elif cs+rem > ps+rem:
        return 'comp'
    else:
        return 'draw'

choices = ['rock','paper','scissors']
os.system('clear')
print('Rock Paper Scissors')
print('Can you win against the computer??')
turns = 0
while True:
    rounds = int(input('How many rounds do you want to play?').strip())
    pc,cc = 0,0
    while True:
        cc = random.choice(choices)
        print(rounds,'Rock ...',end=' ')
        time.sleep(.25)
        print('Paper ...',end=' ')
        time.sleep(.25)
        print('Scissors ...',end=' ')
        time.sleep(.25)
        print('Which one do you choose??')
        time.sleep(.25)
        while pc not in choices:
            pc = input().strip().lower()
        print('Computer :',cc)
        print(compare(pc,cc))
        pc = 0
        print('Player Score    {:^10}'.format(ps))
        print('Computer Score  {:^10}'.format(cs))
        print(turns)
        if (turns >= (rounds/2)+1):
            res =  winCheck(rounds)
            match res:
                case 'player':
                    print('player')
                    break
                case 'comp':
                    print('computer')
                    break
                case 'draw':
                    print('draw')
                    break
    ps,cs,pc,cs,turns = 0,0,0,0,0
    c = input('Do you want to play again?')
    os.system('clear')
    if c == 'n':
        sys.exit(0)



