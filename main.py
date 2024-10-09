from art import logo
import random

# Create a function to calculate the score and handle aces
def calculate_score(cards):
    score = sum(cards)
    # Handle aces: if score > 21 and an ace (11) is in hand, convert ace from 11 to 1
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def blackjack():
    # Player's and dealer's initial cards
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    # Display initial hands
    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    # Check for immediate Blackjack (21) on first deal
    if calculate_score(player_cards) == 21:
        if calculate_score(dealer_cards) == 21:
            print(f"Both you and the dealer have Blackjack! It's a draw!")
        else:
            print(f"🎉 You have Blackjack! You win!")
        return False

    # Player's turn
    while calculate_score(player_cards) < 21:
        choice = input("Type 'Y' to get another card, 'N' to pass: ").upper()
        if choice == 'Y':
            player_cards.append(deal_card())
            print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
        else:
            break

    # Check if player busts (goes over 21)
    if calculate_score(player_cards) > 21:
        print(f"😭 You went over 21! You lose!")
        return False

    # Dealer's turn (dealer must draw until score is 17 or higher)
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

    # Determine the outcome
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    if dealer_score > 21:
        print("🎉 The dealer went over 21! You win!")
    elif player_score == dealer_score:
        print("🤝 It's a draw!")
    elif player_score > dealer_score:
        print("🎉 You win!")
    else:
        print("😭 The dealer wins!")

    return False  # End the game after one round

# Main game loop
choice = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper()

if choice == 'Y':
    continue_game = True
elif choice == 'N':
    continue_game = False
else:
    print("Invalid Input")
    continue_game = False

while continue_game:
    print(logo)
    continue_game = blackjack()  # Play one round and check if the player wants to continue
