import random

def get_user_choice():
    """
    Get user's choice with flexible input options.
    Supports full words, initial letters, and secret bomb functionality.
    """
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or R, P, S): ").strip().lower()
        
        # Check for full words
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        # Check for initial letters and convert to full words
        elif user_choice == "r":
            return "rock"
        elif user_choice == "p":
            return "paper"
        elif user_choice == "s":
            return "scissors"
        # Secret bomb functionality (hidden from user prompts)
        elif user_choice in ["bomb", "b"]:
            return "bomb"
        else:
            print("Invalid choice. Please choose Rock, Paper, Scissors or R, P, S.")

def get_computer_choice():
    """
    Get computer's random choice.
    Computer can also choose bomb (rare occurrence).
    """
    choices = ["rock", "paper", "scissors"]
    # 10% chance for computer to choose bomb
    if random.random() < 0.1:
        choices.append("bomb")
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on game rules including bomb functionality.
    
    Rules:
    - Standard: Rock beats Scissors, Paper beats Rock, Scissors beats Paper
    - Bomb beats Rock and Paper
    - Scissors beats Bomb (defuses it)
    """
    if user_choice == computer_choice:
        if user_choice == "bomb":
            return "It's a tie! Both bombs exploded! 💥💥"
        else:
            return "It's a tie!"
    
    # User wins scenarios
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "scissors" and computer_choice == "bomb")
        or (user_choice == "bomb" and computer_choice in ["rock", "paper"])
    ):
        if user_choice == "bomb":
            if computer_choice == "rock":
                return "You win! Your bomb crushes the rock! 💥🪨"
            elif computer_choice == "paper":
                return "You win! Your bomb burns the paper! 💥📄"
        elif user_choice == "scissors" and computer_choice == "bomb":
            return "You win! Your scissors defused the bomb! ✂️💣"
        else:
            return "You win!"
    
    # Computer wins scenarios
    else:
        if computer_choice == "bomb":
            if user_choice == "rock":
                return "Computer wins! The bomb crushes your rock! 💥🪨"
            elif user_choice == "paper":
                return "Computer wins! The bomb burns your paper! 💥📄"
        elif computer_choice == "scissors" and user_choice == "bomb":
            return "Computer wins! Computer's scissors defused your bomb! ✂️💣"
        else:
            return "Computer wins!"

def display_choices(user_choice, computer_choice):
    """
    Display the choices made by user and computer with appropriate formatting.
    """
    choice_display = {
        "rock": "Rock 🪨",
        "paper": "Paper 📄", 
        "scissors": "Scissors ✂️",
        "bomb": "Bomb 💣"
    }
    
    print(f"You chose: {choice_display.get(user_choice, user_choice.title())}")
    print(f"Computer chose: {choice_display.get(computer_choice, computer_choice.title())}")

def play_game():
    """
    Main game loop with replay functionality.
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("Secret tip: There might be more choices than meets the eye... 😉")
    print()
    
    while True:
        try:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            
            print()
            display_choices(user_choice, computer_choice)
            print()
            
            result = determine_winner(user_choice, computer_choice)
            print(result)
            print()
            
            # Ask if user wants to play again
            while True:
                play_again = input("Play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes', 'n', 'no']:
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            
            if play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye! 👋")
                break
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing! 👋")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Let's try again!")

# Start the game
if __name__ == "__main__":
    play_game()