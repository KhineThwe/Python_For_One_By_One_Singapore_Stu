import random

def get_choices():
    user = input("What is your choice? 'r' for rock,'p' for paper,'s  for scissor\n")  # r
    computer_choice = ['r', 'p', 's']
    computer = random.choice(computer_choice)  # p
    choices = {"player":user,"computer":computer}
    return choices

def check_win(player,computer):
    if player == computer:
        return "It's a tie"
    elif player == "r":
        if computer == "p":
            return "Paper covers rock!You lose!"
        elif computer == "s":
            return "Rock smashes scissors!You win!"
    elif player == "p":
        if computer == "r":
            return "Paper covers rock!You win!"
        elif computer == "s":
            return "Scissors cuts paper!You lose!"
    elif player == "s":
        if computer == "p":
            return "Scissors cuts paper!You win!"
        elif computer == "r":
            return "Rock smashes scissors!You lose!"

c = get_choices() #{"player":"","computer":""}
print("Player and computer choice ",c)
print("Player choice: ",c.get("player"))
print("Computer choice: ",c.get("computer"))

result = check_win(c.get("player"),c.get("computer"))
print(result)