import os
clear = lambda: os.system('clear')
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bid_list={}
is_continue=True

while is_continue:
  name=input("What is your name?\n")
  bid=int(input("What is your bid?\n"))
  new_bid={name:bid}
  bid_list.update(new_bid)
  to_continue=input("Is there any other person? Type y or n: ")
  clear()
  if to_continue=="n":
    is_continue=False
control_number=0
for bids in bid_list:
  if bid_list[bids]>control_number:
    control_number=bid_list[bids]
    winner=bids
print(f"Maximum bid is {winner}'s bid with {control_number}$")
"""    
for name, bid in bid_list.items():
    if control_number == bid:
        print(f"Maximum bid is {name}'s bid with {control_number}$")
"""