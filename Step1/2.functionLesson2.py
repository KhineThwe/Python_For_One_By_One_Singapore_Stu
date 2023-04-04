#simple ver of rock paper scissor
import random
def play():
    user = input("Enter r for rock,p for paper,s for scissors")
    computer = random.choice(['r','p','s'])
    print('User chooses {} , Computer chooses {}'.format(user,computer))

    if user == computer:
        tie(user,computer)
    if is_win(user,computer):#if True:
        return "You win"
    else:
       return "You lost!"


def tie(player,computer):
    if player == computer:
        return "It is a tie"

def is_win(player,computer):
    #player r ----> s
    #player s ---> p
    #player p ---> r
    if(player == 'r' and computer=="s") or (player == 's' and player=='p') or (player == 'p' and computer == 'r'):
        return True

result = play()
print(result)
