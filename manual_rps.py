import random 
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)
def get_user_choice():
    choice = input("give your choice:")
    return choice
    
