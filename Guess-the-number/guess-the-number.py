from art import logo

print(logo)

print("Welcome to the number guessing game")
print("Im thinking of a number between 1 to 100")

import random

number = random.randint(1,100)

# print(number)

difficulty=input("Select your difficulty, Type 'easy' or 'hard' :")

if difficulty == 'easy':
    lives=10
elif difficulty == 'hard':
    lives=5
Game_over=False
while (lives != 0) and (not Game_over):
    
    print(f"You have {lives} attempt to guess the number")
    guess=int(input("Make a guess :"))
    
    if guess == number:
        print(f"You got it,The answer is {number}")
        Game_over=True
    elif guess < number:
        print("Too Low \nGuess again")
        lives-=1
    elif guess > number:
        print("Too High \nGuess again")
        lives-=1

if lives == 0:
    print("You have run out of lives, you lose")
