import random 
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)
def get_user_choice():
    choice = input("give your choice:")
    return choice
def get_winner(computer_choice, user_choice):
    computer=computer_choice
    user = user_choice
    if computer == 'Rock' and user == 'Scissors' or computer =='Paper' and user=='Rock' or computer=='Scissors' and user=='Paper':
        print("You lost")
    elif user == 'Rock' and computer == 'Scissors' or user =='Paper' and computer=='Rock' or user=='Scissors' and computer=='Paper':
        print("You won!")
    else:
        print("It is a tie!")