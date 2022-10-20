from game_data import data
import random
from art import logo
from art import vs
from replit import clear

score=0

game_over=False



A=random.choice(data)

while not game_over:
    print(logo)
    
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} followers {A['follower_count']}")
    
    B=random.choice(data)
    
    print(vs)
    
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']} followers {B['follower_count']}")
    
    if A['follower_count'] > B['follower_count']:
        greater = A
    else:
        greater= B
    
    def check(guessed_option,last_option,greater):
        clear()
        global score
        if guessed_option == greater:
            score+=1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry thats wrong.Final score: {score}")
            return True
    
        
    
    if input("Who has more followers? Type 'A' or 'B' ") ==  'A':
        game_over=check(A,B,greater)
    else:
        game_over=check(B,A,greater)
    A=B
