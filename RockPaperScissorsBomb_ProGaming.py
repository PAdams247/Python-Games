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
    
    Returns: ('user', 'computer', 'tie', message)
    """
    if user_choice == computer_choice:
        if user_choice == "bomb":
            return 'tie', "It's a tie! Both bombs exploded! 💥💥"
        else:
            return 'tie', "It's a tie!"
    
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
                return 'user', "You win! Your bomb crushes the rock! 💥🪨"
            elif computer_choice == "paper":
                return 'user', "You win! Your bomb burns the paper! 💥📄"
        elif user_choice == "scissors" and computer_choice == "bomb":
            return 'user', "You win! Your scissors defused the bomb! ✂️💣"
        else:
            return 'user', "You win!"
    
    # Computer wins scenarios
    else:
        if computer_choice == "bomb":
            if user_choice == "rock":
                return 'computer', "Computer wins! The bomb crushes your rock! 💥🪨"
            elif user_choice == "paper":
                return 'computer', "Computer wins! The bomb burns your paper! 💥📄"
        elif computer_choice == "scissors" and user_choice == "bomb":
            return 'computer', "Computer wins! Computer's scissors defused your bomb! ✂️💣"
        else:
            return 'computer', "Computer wins!"

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

def display_score(user_score, computer_score, ties, round_num=None, total_rounds=None):
    """
    Display current score with formatting.
    """
    print("=" * 50)
    if round_num and total_rounds:
        print(f"ROUND {round_num}/{total_rounds} COMPLETE")
    print(f"SCORE: You {user_score} - {computer_score} Computer | Ties: {ties}")
    
    total_games = user_score + computer_score + ties
    if total_games > 0:
        user_percentage = (user_score / total_games) * 100
        computer_percentage = (computer_score / total_games) * 100
        tie_percentage = (ties / total_games) * 100
        print(f"Win Rate: You {user_percentage:.1f}% - {computer_percentage:.1f}% Computer | Ties: {tie_percentage:.1f}%")
    print("=" * 50)

def get_game_mode():
    """
    Get the game mode from user.
    """
    print("\n🎮 GAME MODE SELECTION 🎮")
    print("1. Best 2 out of 3 rounds")
    print("2. Best 3 out of 5 rounds") 
    print("3. First to 5 wins")
    print("4. First to 10 wins")
    print("5. First to 21 wins")
    print("6. Unlimited rounds (play until you quit)")
    
    while True:
        try:
            choice = input("\nSelect game mode (1-6): ").strip()
            if choice == "1":
                return "best_of", 3, 2  # best of 3, need 2 wins
            elif choice == "2":
                return "best_of", 5, 3  # best of 5, need 3 wins
            elif choice == "3":
                return "first_to", None, 5  # first to 5 wins
            elif choice == "4":
                return "first_to", None, 10  # first to 10 wins
            elif choice == "5":
                return "first_to", None, 21  # first to 21 wins
            elif choice == "6":
                return "unlimited", None, None  # unlimited
            else:
                print("Invalid choice. Please select 1-6.")
        except ValueError:
            print("Invalid input. Please enter a number 1-6.")

def check_game_end(mode, user_score, computer_score, ties, max_rounds, target_wins):
    """
    Check if the game should end based on the mode and current scores.
    Returns (game_ended, winner, reason)
    """
    total_games = user_score + computer_score + ties
    
    if mode == "best_of":
        # Check if someone reached target wins or max rounds played
        if user_score >= target_wins:
            return True, "user", f"You won the best of {max_rounds} series!"
        elif computer_score >= target_wins:
            return True, "computer", f"Computer won the best of {max_rounds} series!"
        elif total_games >= max_rounds:
            if user_score > computer_score:
                return True, "user", f"You won the series {user_score}-{computer_score}!"
            elif computer_score > user_score:
                return True, "computer", f"Computer won the series {computer_score}-{user_score}!"
            else:
                return True, "tie", f"Series ended in a tie {user_score}-{computer_score}!"
    
    elif mode == "first_to":
        if user_score >= target_wins:
            return True, "user", f"You reached {target_wins} wins first!"
        elif computer_score >= target_wins:
            return True, "computer", f"Computer reached {target_wins} wins first!"
    
    return False, None, None

def display_final_stats(user_score, computer_score, ties):
    """
    Display comprehensive final game statistics.
    """
    total_games = user_score + computer_score + ties

    print("\n" + "🏆" * 20 + " FINAL STATISTICS " + "🏆" * 20)
    print(f"Total Games Played: {total_games}")
    print(f"Your Wins: {user_score}")
    print(f"Computer Wins: {computer_score}")
    print(f"Ties: {ties}")

    if total_games > 0:
        user_percentage = (user_score / total_games) * 100
        computer_percentage = (computer_score / total_games) * 100
        tie_percentage = (ties / total_games) * 100

        print(f"\nWin Percentages:")
        print(f"You: {user_percentage:.1f}%")
        print(f"Computer: {computer_percentage:.1f}%")
        print(f"Ties: {tie_percentage:.1f}%")

        # Determine overall winner
        if user_score > computer_score:
            print(f"\n🎉 CONGRATULATIONS! You won overall! 🎉")
            print(f"Victory margin: +{user_score - computer_score} wins")
        elif computer_score > user_score:
            print(f"\n🤖 Computer won overall! Better luck next time! 🤖")
            print(f"Defeat margin: -{computer_score - user_score} wins")
        else:
            print(f"\n🤝 Overall result: Perfect tie! 🤝")

    print("🏆" * 58)

def play_game():
    """
    Main game loop with scoring and multiple game modes.
    """
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("Secret tip: There might be more choices than meets the eye... 😉")
    
    # Get game mode
    mode, max_rounds, target_wins = get_game_mode()
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    ties = 0
    round_num = 0
    
    print(f"\n🚀 Starting game! 🚀")
    if mode == "best_of":
        print(f"Playing best {target_wins} out of {max_rounds} rounds")
    elif mode == "first_to":
        print(f"Playing first to {target_wins} wins")
    else:
        print("Playing unlimited rounds - quit anytime!")
    
    while True:
        try:
            round_num += 1
            print(f"\n--- ROUND {round_num} ---")
            
            # Display current score
            if round_num > 1:
                display_score(user_score, computer_score, ties)
                print()
            
            # Get choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            
            print()
            display_choices(user_choice, computer_choice)
            print()
            
            # Determine winner and update scores
            winner, message = determine_winner(user_choice, computer_choice)
            print(message)
            
            if winner == 'user':
                user_score += 1
            elif winner == 'computer':
                computer_score += 1
            else:
                ties += 1
            
            # Check if game should end
            game_ended, _, end_reason = check_game_end(
                mode, user_score, computer_score, ties, max_rounds, target_wins
            )
            
            if game_ended:
                print(f"\n🎯 {end_reason}")
                display_score(user_score, computer_score, ties)
                display_final_stats(user_score, computer_score, ties)
                break
            
            # For unlimited mode, ask if user wants to continue
            if mode == "unlimited":
                print()
                display_score(user_score, computer_score, ties, round_num)
                while True:
                    continue_game = input("\nContinue playing? (y/n): ").strip().lower()
                    if continue_game in ['y', 'yes', 'n', 'no']:
                        break
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                
                if continue_game in ['n', 'no']:
                    display_final_stats(user_score, computer_score, ties)
                    break
            
        except KeyboardInterrupt:
            print("\n\n🛑 Game interrupted!")
            if round_num > 1:
                display_final_stats(user_score, computer_score, ties)
            print("Thanks for playing! Goodbye! 👋")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Let's try again!")
    
    # Ask if user wants to play again with different settings
    print("\n" + "="*50)
    while True:
        play_again = input("Start a new game with different settings? (y/n): ").strip().lower()
        if play_again in ['y', 'yes']:
            play_game()  # Recursive call for new game
            break
        elif play_again in ['n', 'no']:
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Start the game
if __name__ == "__main__":
    play_game()