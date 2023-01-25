import random 
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)
def get_user_choice():
    choice = input("give your choice:")
    return choice
def get_winner():
    computer = get_computer_choice()
    user = get_computer_choice()
    if computer == 'Rock' and user == 'Scissors' or computer =='paper' and user=='Rock' or computer=='Scissors' and user=='Paper':
        print("You lost")
    elif user == 'Rock' and computer == 'Scissors' or user =='paper' and computer=='Rock' or user=='Scissors' and computer=='Paper':
        print("You won!")
    else:
        print("It is a tie!")