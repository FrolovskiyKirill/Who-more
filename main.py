import game_data
import logo
import random
from replit import clear

print(logo.logo)
SCORE_COUNTER = 0

def game():
  first_data = game_data.data[random.randint(0, len(game_data.data) - 1)]
  second_data = game_data.data[random.randint(0, len(game_data.data) - 1)]
  
  # print(first_data)
  # print(second_data)
  
  first_name = first_data["name"]
  first_follower_count = first_data["follower_count"]
  first_description = first_data["description"]
  first_country = first_data["country"]
  
  second_name = second_data["name"]
  second_follower_count = second_data["follower_count"]
  second_description = second_data["description"]
  second_country = second_data["country"]
  
  global SCORE_COUNTER
  
  print(f"Compare A: {first_name}, a {first_description}, from {first_country}")
  print(logo.vs)
  print(f"Against B: {second_name}, a {second_description}, from {second_country}")
  user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if user_answer == "a" and first_follower_count > second_follower_count:
    SCORE_COUNTER += 1
    clear()
    print(f"You'right! Current score: {SCORE_COUNTER}")
    game()
  elif user_answer == "b" and first_follower_count < second_follower_count:
    SCORE_COUNTER += 1
    clear()
    print(f"You'right! Current score: {SCORE_COUNTER}")
    game()
  elif first_follower_count == second_follower_count:
    clear()
    game()
  else:
    clear()
    print(f"Sorry, that's wrong. Final score: {SCORE_COUNTER}")

game()
