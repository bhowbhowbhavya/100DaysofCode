import sys
import random
from Blackjack_logo import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

user_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]


play = input("Do you want to play a game of blackjack?, type 'y' or 'n'")
if play == "y": 
    print(logo)
    should_continue = True
    print(user_cards, sum(user_cards))
    print(computer_cards[0])
    while should_continue:    
        sum_user_cards=sum(user_cards)
        sum_computer_cards=sum(computer_cards)
        if sum_user_cards==21 or sum_computer_cards==21:
            if sum_computer_cards==21 and len(user_cards)==2:
                print("You lose with comp Black Jack", computer_cards)
                should_continue = False
                sys.exit(0)
            else:
                print("You win your sum is 21 with more than 2 cards!")
                should_continue = False
                sys.exit(0)
        else:
            if sum_user_cards>21:
                if 11 in user_cards:
                    i = user_cards.index(11)
                    user_cards[i]=1
                    sum_user_cards = sum(user_cards)
                    print(sum(user_cards))
                if sum_user_cards>21: #check with new sum_cards
                    print("You lose coz ur sum is more than 21!")
                    should_continue = False
                    sys.exit(0)
            else:
                want_a_new_card= input("Do you want a new card?, type 'y' or 'n'")            
                if want_a_new_card == "y":
                    user_cards.append(deal_card())
                    sum_user_cards=sum(user_cards)
                    print(user_cards, sum_user_cards)
                    print(computer_cards[0])
                else:
                    should_continue = False #lets computer play the game
    while sum_computer_cards<17 and sum_user_cards<=21:
        computer_cards.append(deal_card())
        sum_computer_cards=sum(computer_cards)
        if 11 in computer_cards:
            i = computer_cards.index(11)
            computer_cards[i]=1
            sum_computer_cards = sum(computer_cards)
            print(sum(computer_cards)) 
    #final comparison                         
    if sum_computer_cards>21 and sum_user_cards<=21:
       print("Dealer busted.You win!")
    else:
        if sum_user_cards>sum_computer_cards:
            print("You win: final check!")
            sys.exit(0)
        elif sum_user_cards==sum_computer_cards:
            print("Game is draw: final check!")
            sys.exit(0)
        else:
            print("You lose:: final check!", sum_computer_cards)
            sys.exit(0)
            
else:
    print("Goodbye for the day!")          