import random
import os
import art


# Function to deal a random card
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Function to calculate the score
def calculate_score(cards):
    """Calculates the total score of the given cards."""

    # Check for a blackjack (Ace + 10)
    if len(cards) == 2 and 11 in cards and 10 in cards:
        return 0  # Blackjack

    # Calculate total score
    total = sum(cards)

    # If score is over 21 and there's an Ace (11), convert it to 1
    while total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)

    return total

print(art.logo)
# Function to compare scores
def compare(user_score, computer_score):
    """Compares the final scores and determines the winner."""
    if user_score == computer_score:
        return "It's a draw! 🤝"
    elif computer_score == 0:
        return "Computer has a Blackjack! You lose! 😭"
    elif user_score == 0:
        return "You have a Blackjack! You win! 🎉"
    elif user_score > 21:
        return "You busted! Computer wins! 😭"
    elif computer_score > 21:
        return "Computer busted! You win! 🎉"
    elif user_score > computer_score:
        return "You win! 🎉"
    else:
        return "Computer wins! 😭"


# Main function to start the game
def play_blackjack():
    """Runs the main game loop."""
    print("\nWelcome to Blackjack! 🃏")

    # Initialize user and computer hands
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        # Calculate initial scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show user and computer first card
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game should end immediately
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want another card
            user_choice = input("Do you want another card? Type 'y' for yes, 'n' for no: ").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())  # Add new card
            else:
                game_over = True  # User stops drawing

    # Let the computer play: keep drawing if score is less than 17
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and result
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Determine the winner


# Run the game loop
while True:
    play_blackjack()

    # Ask the user if they want to play again
    replay = input("\nDo you want to play again? Type 'y' for yes, 'n' for no: ").lower()
    if replay == 'n':
        print("Thanks for playing! Goodbye! 👋")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console before new game
