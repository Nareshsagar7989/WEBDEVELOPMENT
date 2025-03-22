import random

def get_computer_choice():
    """
    Generates a random choice (rock, paper, or scissors) for the computer.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """
    Plays a round of Rock-Paper-Scissors.
    """
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"\nComputer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    """
    Main function that runs the game.
    """
    play_again = "yes"
    user_score = 0
    computer_score = 0

    while play_again.lower() == "yes":
        play_game()
        result = determine_winner(input("Enter your choice (rock, paper, or scissors): ").lower(), get_computer_choice())
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()