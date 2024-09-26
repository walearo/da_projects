import random

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

# Main function
def play_game():
    choices = ["Rock", "Paper", "Scissors"]
    
    # Player input
    player_choice = input("Enter: Rock, Paper, or Scissors: ").capitalize()
    
    # Validate player input
    if player_choice not in choices:
        print("Invalid input! Please enter: Rock, Paper, or Scissors.")
        return
    
    # Computer randomly chooses
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

while True:
    # Run the game
    play_game()

    # Check if player likes to play again.
    response = input("Do you want to play again? Y or N: ")
    if response.upper() == "N":
        print("Thank you for playing, Goodbye!")
        break