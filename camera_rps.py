import cv2
from keras.models import load_model
import numpy as np
import time
import random
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_prediction():
    start = time.time()
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print('the result is:',prediction)
    end = time.time()
    print('Single round cost:' ,end-start,'s')
    return prediction

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)
def get_winner(computer_choice, user_choice):
    computer=computer_choice
    user = user_choice
    if computer == 'Rock' and user == 'Scissors' or computer =='Paper' and user=='Rock' or computer=='Scissors' and user=='Paper':
        return -1
    elif user == 'Rock' and computer == 'Scissors' or user =='Paper' and computer=='Rock' or user=='Scissors' and computer=='Paper':
        return 1
    else:
        return 0

computer_wins=0
user_wins=0
rounds_played=0

for i in range(6):
    user = get_prediction()
    user = np.argmax(user)
    choices = ['Rock', 'Paper', 'Scissors']
    user = choices[user]
    computer = get_computer_choice()
    winner = get_winner(computer,user)
    if winner == -1:
        computer_wins+=1
    elif winner == 1:
        user_wins +=1
    else:
        i-=1
    if user_wins ==3:
        print("User wins")
    if computer == 3:
        print("Computer wins")
    rounds_played +=1
    if rounds_played==5:
        print("End the game")

