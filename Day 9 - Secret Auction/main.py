from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
bidding_finished = False

bids = {}


def find_highest_bidder(bidding_record):
  highest_bid = 0

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {bidder} with the bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is you name?")
  price = int(input("What is your bid? $"))
  
  bids[name] = price
  should_continue = input("Are there any oher bidders? Type 'Yes' or 'No'. ")
  
  if should_continue == "no":
    bidding_finished= True
    find_highest_bidder(bids)

  elif should_continue == "yes":
    clear()