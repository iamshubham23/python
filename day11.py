#blackjack-project
import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:   
        print("it's a draw")
    elif computer_score==0:
        print("you loose")
    elif user_score==0:
        print("you win")
    elif user_score > 21:
        print("you loose")
    elif computer_score > 21:
        print("you win")
    elif user_score > computer_score:
        print("you win")
    else:
        print("you loose")           

def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    for _ in range(2):
        new_card=deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards: {user_cards},current score:{user_score}")
        print(f"computer's first card {computer_cards[0]}:")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("want to withdraw another card if yes type 'y' ortherwise 'n'")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True    
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"computer final {computer_cards},final_score {computer_score}")
    compare(user_score,computer_score)
while input("do you want to play a game of blackjack type y or n")=="y":
    play_game()    