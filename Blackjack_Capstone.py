import random
from replit import clear

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif user_score == 0:
        return"you won,you got a blackjack"
    elif dealer_score == 0:
        return "you lose, Dealer got a black jack"
    elif user_score > 21:
        return "you lose"
    elif dealer_score > 21:
        return "you win"
    elif user_score > dealer_score:
        return "you win"
    else:
        return "you lose"


def start_game():
    user_cards = []
    dealer_cards = []
    game_over = False
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        dealer_cards.append(new_card)
        
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"your cards {user_cards} and your score = {user_score}")
    print(f"Dealer's first card is :- {dealer_cards[0]}")

    while not game_over:
        if user_score == 0 or dealer_score == 0 or user_score >21 :
            game_over = True
        else :
            additional_card = input("if you want to draw another card.Type 'y'\n To pass Type 'n' :- ")
            if additional_card == "y":
                user_cards.append(deal_card())
                print(f"user cards are {user_cards}")
                print(calculate_score(user_cards))
            else:
                game_over = True

    while dealer_score !=0 and dealer_score <17:
        dealer_cards.append(deal_card)
        dealer_score = calculate_score(dealer_cards)
        print(f"dealer cards are {dealer_cards} and his score {dealer_score}")

    compare(user_score,dealer_score)

start_game()
while input("To restart the game.Type 'y' to end type 'n' :- ") == "y":
    clear()
    start_game()