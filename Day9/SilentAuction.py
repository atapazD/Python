import art
print(art.logo)

bids={}
continue_bid = True

def find_highest_bidder(bidding_dictionary):
    highest_bid= 0
    winner = ""

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print (f"The winner is....{winner}!!!!")

while continue_bid:
    user_name = input("What is your name?")
    user_bid = int(input("what is your bid?"))

    bids[user_name]= user_bid

    next_bid = input("New bid?\n Please enter 'y' or 'n'.\n").lower()

    if next_bid == 'n':
        continue_bid = False
        find_highest_bidder(bids)
    else:
        print ("\n"* 100)

