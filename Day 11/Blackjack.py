import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)
player_hand = []
dealer_hand = []
gameOver = False
def text_space():
    print("\n" * 5)
def deal_card(hand):
    hand.append(random.choice(cards))

def show_hand():
    print (f"Player hand:{player_hand} Total:{sum(player_hand)} \nDealer hand:{dealer_hand} Total:{sum(dealer_hand)}")   


deal_card(player_hand)
deal_card(player_hand)
deal_card(dealer_hand)
show_hand()

while gameOver == False: 
    if sum(player_hand) == 21:
        print("You got BlackJack. You win!")
        # show_hand()
        gameOver = True
    elif sum(player_hand) > 21:
        print("You bust, sorry you lose!")
        # show_hand()
        gameOver = True
    else:
        choice = input("Would you like to hit = 'y' or stand = 'n'?\n")

        if choice == 'y':
            deal_card(player_hand)
            text_space()
            show_hand()
            choice = ""
        else:
            while sum(dealer_hand) < 16:
                deal_card(dealer_hand)
                text_space()
                show_hand()

                if sum(dealer_hand) == 21:
                    print ("You lose")
                    gameOver = True
                elif sum(dealer_hand) > 21:
                    print("Dealer busts, You win!")
                    gameOver = True
            if sum(player_hand) > sum(dealer_hand):
                print("You win!!!")
                gameOver = True
            elif sum(player_hand) < sum(dealer_hand):
                print("You lose!")
                gameOver = True
            elif sum(player_hand) == sum(dealer_hand):
                print("Its a Draw!")
                gameOver = True    


        


