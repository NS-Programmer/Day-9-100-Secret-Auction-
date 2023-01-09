import art 
from replit import clear


def calculate_bidder (list1): 
  highest = 0
  name = "" 
  for key in list1: 
    bid = list1[key]
    if bid > highest: 
      highest = bid
      name = key 
  print (f"The winner is {name} with a bid of $ {highest}")

print (art.logo)
print ("Welcome to the secret auction program.")

auction = {} 
user_input = True

while user_input == True: 
  name = input("What is your name?")
  bid_amt = input("What's your bid?")
  bid_amt = int(bid_amt)
  auction[name] = bid_amt
  
  bid_Again = input("Are there any other bidders? Type yes or no.")
  bid_Again.lower()
  
  if bid_Again == "yes": 
    clear()
  else:
    clear()
    user_input = False

calculate_bidder(auction)
