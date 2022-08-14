import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(list):
  score = 0
  for length in range(len(list)):
    score += list[length]
  if score == 21 and len(list) == 2:
    score = 0 #blackjek spotted
  if score > 21 and 11 in list:
    score -= 10
  return score

def compare():
  if user_score == computer_score:
    return "It's a Draw"
  elif user_score == 0:
    return ("User Wins")
  elif computer_score == 0:
    return "Computer Wins"
  elif computer_score > 21:
    return ("User Wins")
  elif user_score > 21:
    return "Computer Wins"
  elif computer_score < user_score:
    return "User Wins"
  else:
    return "Computer Wins"
   
#main
is_all_over = False

while(not is_all_over):
  is_over = False
  
  user_cards = []
  computer_cards = []
  
  for two in range(2): #dealing first two cards each
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while(not is_over): #User's play
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"User Cards: {user_cards}\t\t Score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_over = True
    else:
      user_prompt = input("Do you want to draw a card? (y/n) ")
      if user_prompt == "y":
        user_cards.append(deal_card())
      else:
        is_over = True
  
  while (computer_score < 17 and computer_score != 0): #Computer's play
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  #declaring the winner
  print(f"Computer Cards: {computer_cards}\t\t Score: {computer_score}")
  print(compare())

  again = input("Wanna Play Again? (y/n)")
  clear()
  if(again == "n"):
    is_all_over = True