
# Blackjack Game

A simple command-line Blackjack game written in Python. This project simulates the classic card game where you, the player, compete against the dealer to get as close to 21 points as possible without going over.

## Features
- **Player vs Dealer:** Play against the dealer and try to beat their hand without exceeding 21.
- **Automatic Ace Handling:** Aces are automatically treated as either 11 or 1, depending on the player's total score.
- **Dealer's Rules:** The dealer must draw cards until their score is at least 17.
- **Blackjack:** If either the player or the dealer gets 21 on the first two cards, it's an instant win (or draw if both get 21).
- **User Input:** Players can decide whether to draw another card or pass after their initial hand.

## How to Play

1. Clone the repository and run the game on your machine.
2. When prompted, enter `'Y'` to start a game of Blackjack or `'N'` to quit.
3. Once the game starts, you'll be dealt two cards. You can see your current score and the dealer's first card.
4. If your score isn't 21, you'll have the option to draw another card (`'Y'`) or pass (`'N'`).
5. The dealer will then reveal their hand and draw additional cards until they reach a score of at least 17.
6. The game will determine the winner based on who has the higher score without exceeding 21.

## Rules

- **Card Values:**
  - Number cards (2-10) are worth their face value.
  - Face cards (J, Q, K) are each worth 10 points.
  - Aces can be worth 11 or 1, depending on which value would be more beneficial without exceeding 21.

- **Winning Conditions:**
  - If your initial two cards total 21, it's a Blackjack! You win unless the dealer also has a Blackjack (in which case, it’s a draw).
  - If your total score is higher than the dealer's without exceeding 21, you win.
  - If your score exceeds 21, you "bust" and lose.
  - If the dealer's score exceeds 21, the dealer busts and you win.

## Installation and Running

1. Clone the repository:

   ```bash
   git clone https://github.com/JasperMunene/black-jack.git
   ```

2. Navigate to the project directory:

   ```bash
   cd black-jack
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to play the game.

## Project Structure

```
blackjack-game/
│
├── art.py            # Contains ASCII art for the game logo
├── main.py           # Main Blackjack game script
└── README.md         # Documentation for the project
```

## Dependencies

- **Python 3.x** is required to run the game.

## Future Enhancements

- Add the option to play multiple rounds without restarting the program.
- Implement betting and tracking the player's total money.
- Allow more than one player to play at a time.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

