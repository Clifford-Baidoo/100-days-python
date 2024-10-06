from art import logo

print(logo)
bids = {}  # Dictionary to store bids
question = False

def bidding(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main loop to handle bidding
while not question:
    name1 = input("What is your name:\n")
    bid1 = int(input("How much will you bid:\n"))
    bids[name1] = bid1  # Store bid in the dictionary

    continue_bidding = input("Do you want to bid again? yes or no \n").lower()

    if continue_bidding == "no":
        question = True  # Stop the loop if the user says "no"
        print("Bids locked in")
        bidding(bids)  # Call the bidding function to determine the winner
    elif continue_bidding == "yes":
        print("Enter bidder details")





