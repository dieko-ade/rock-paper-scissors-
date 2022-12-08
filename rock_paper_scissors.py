import random

# returns the choices of the player and computer
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ").lower().strip()
  
  if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
    raise Exception("Oops, you made an invalid play choice. I was expecting rock, paper, or scissors (you don't have to worry about the sentence case).")
    
  play_options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(play_options)
  choices = {"player": player_choice.lower(), "computer": computer_choice}
  return choices

# checks for the outcome of each round based on the choices of the player and computer
def check_win(player, computer):
  print(f"You played {player}, and the computer played {computer}")
  
  winner = ""
  outcome_message = ""
  
  if player == computer: 
    winner = "None"
    outcome_message = "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      winner = "player"
      outcome_message = "Rock smashes scissors! You win!"
    else: 
      winner = "computer"
      outcome_message =  "Paper covers rock! You lose"
  elif player == "paper":
    if computer == "rock":
      winner = "player"
      outcome_message = "Paper covers rock! You win!"
    else:
      winner = "computer"
      outcome_message = "Scissors cuts paper! You lose"
  else:
    if computer == "paper":
      winner = "player"
      outcome_message = "Scissors cuts paper! You win!"
    else:
      winner = "computer"
      outcome_message  = "Rock smashes scissors! You lose"
      
  return [winner, outcome_message]

#starts the game 
def start_game():
  max_wins = input("Enter how many wins to end the game: ")

  if not max_wins.isdecimal():
    raise Exception(f"Haha, you can't win a game {max_wins} times. I was expecting an integer value.")

  max_wins, player_wins, computer_wins, tied_rounds = int(max_wins), 0, 0, 0
  
  while player_wins < max_wins and computer_wins < max_wins:
    choices = get_choices()
    outcome = check_win(choices["player"], choices["computer"])

    if (outcome[0] == "player"):
      player_wins += 1
    elif (outcome[0] == "computer"):
      computer_wins += 1
    else:
      tied_rounds += 1
      
    print(outcome[1])
    print(f"You have won {player_wins} game(s), and the computer has won {computer_wins} game(s).\n")

  if (player_wins == max_wins):
    print("Woohoo🥳! You won the game!")
  else:
    print("You lost the game. That sucks, you'll get it next time.")

  want_game_summary = input("Do you want a summary of the game? (Enter Y or N)").upper().strip()
  if want_game_summary != "Y" and want_game_summary != "N":
    raise Exception("You entry was invalid. A Y or N would do (no need to worry about the sentence case")

  if (want_game_summary == "Y"):
    print(f" You won {player_wins} round(s) and the computer won {computer_wins} round(s)! \n{tied_rounds} round(s) resulted in a tie. In total, you played {player_wins + computer_wins + tied_rounds} round(s) against the computer.")
  print("Thanks for playing! Come again next time.")
  
start_game()