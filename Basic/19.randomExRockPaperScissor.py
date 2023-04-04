import random


def get_choices():
    user = input("What is your choice? 'r' for rock,'p' for paper,'s  for scissor\n")  # r
    computer_choice = ['r', 'p', 's']
    computer = random.choice(computer_choice)  # p
    print(computer)

    if user == computer:
        return "It's a tie"
    elif user == "r":
        if computer == "p":
            return "Paper covers rock!You lose!"
        elif computer == "s":
            return "Rock smashes scissors!You win!"
    elif user == "p":
        if computer == "r":
            return "Paper covers rock!You win!"
        elif computer == "s":
            return "Scissors cuts paper!You lose!"
    elif user == "s":
        if computer == "p":
            return "Scissors cuts paper!You win!"
        elif computer == "r":
            return "Rock smashes scissors!You lose!"


choice = get_choices()
print(choice)
