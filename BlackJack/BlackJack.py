from replit import clear
import random
from art import logo

while input("Do you want to start a game of BlackJack y/n :")=='y':
    clear()
    print(logo)
    
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    
    user_cards = []
    computer_cards = []
    
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
    Game_over=False
    
    def calculate_score(card_list):
        score=sum(card_list)
        if 11 in card_list and 10 in card_list and len(card_list) == 2:
            return 0
        elif score >21 and 11 in card_list:
            card_list.remove(11)
            card_list.append(1)
        else:
            return score
    
    
    computer_score=calculate_score(computer_cards)
    while not Game_over:
        user_score=calculate_score(user_cards)
        
        print(f"     Your cards are {user_cards}, your score is {user_score}")
        print(f"     The computers first card {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            Game_over=True
        else:    
            if input("Do you want to draw another card  y/n :") == 'y':
                user_cards.append(deal_card())
            else:
                Game_over = True
        
    while computer_score != 0 and computer_score < 12:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
            
    def compare(uscore,cscore):
        if uscore == cscore:
            print("Its a draw")
        elif uscore == 0:
            print("Its a blackJack, You win")
        elif cscore == 0:
            print("Its a blackJack, You lose")
        elif uscore > 21:
            print("You went over 21,You lose")
        elif cscore > 21:
            print("they went over 21,You win")
        elif uscore > cscore:
            print("You win")
        elif uscore < cscore:
            print("You lose")
            y
        
    compare(user_score,computer_score)
    print(f"The computers cards were {computer_cards}, the score was {computer_score}")
    print(f"Your cards were {user_cards}, the score was {user_score}")
