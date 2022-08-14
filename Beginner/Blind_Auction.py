from replit import clear #used clear() to clear the console

is_other_person = True
biders = {}
#Takes all the inputs and feed into the Dictionary
while (is_other_person):
  person = input("Name of the person: ")
  value = int(input("How much do you want to bid?" $))
  biders[person] = value

  is_other = input("Is there any other bidder? ")
  clear()
  if(is_other == "no"):
    is_other_person = False

#to keep track of the Winner
highest_bid = 0
highest_bider = ''

#Winner decider 
for values in biders:
  print(biders[values])
  if (highest_bid < biders[values]):
    highest_bid = biders[values]
    highest_bider = values

#Prints the winner
print(f"So, {highest_bider} wins because he bids for ${highest_bid}")