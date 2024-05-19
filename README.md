# Blackjack
This is a tiny blackjack program I coded as my first program for a university course. have fun playing around.

## Features

- Simple and intuitive GUI using Tkinter.
- Ability to place bets and manage balance.
- Dealer plays automatically following standard Blackjack rules.
- Option to start a new round or leave the table and take the money.
- Displays the outcome of each round and updates the balance accordingly.

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)
- Pillow library for image handling

## Installation

1. Clone this repository or download the source code.
2. Ensure you have the required libraries installed. You can install Pillow using pip:
    ```sh
    pip install pillow
    ```

## Card Images

Place the card images in a folder named `card_images` within the same directory as your script. The images should be named in the format `<rank>_of_<suit>.png`, e.g., `2_of_hearts.png`, `jack_of_spades.png`, etc.

## How to Play

1. Run the script:
    ```sh
    python blackjack.py
    ```
2. Enter your bet and click the "Place Bet" button.
3. Use the "Hit" button to draw a card and the "Stay" button to hold your total.
4. The dealer will play automatically after you choose to stay.
5. The outcome of the round will be displayed and your balance will be updated.
6. Click "New Round" to start a new game or "Leave Table and Take Money" to end the session.
7. When you choose to leave, your final balance will be displayed. Click "Close Program" to exit the game.

## Code Overview

### Main Functions

- `load_images(card_images)`: Loads card images, resizes them, and adds them to the `card_images` list.
- `deal_card(frame)`: Deals the next card from the deck and adds it to the specified frame.
- `calculate_points(hand)`: Calculates the total points of a hand.
- `dealer_plays()`: Handles the dealer's turn.
- `player_hits()`: Handles the player's turn when they draw a card.
- `initial_deal()`: Deals the initial cards to the player and the dealer.
- `new_round()`: Starts a new round by resetting hands and updating the UI.
- `reset_frames()`: Resets the frames for dealer and player cards.
- `shuffle_deck()`: Shuffles the deck.
- `update_balance(player_wins)`: Updates the player's balance based on the outcome of the round.
- `ask_for_bet()`: Prompts the player to enter their bet.
- `place_bet()`: Places the player's bet and starts the initial deal.
- `determine_winner()`: Determines the winner of the round.
- `end_round()`: Ends the current round and enables appropriate buttons.
- `leave_table()`: Displays the player's final balance and enables the end game button.
- `end_game()`: Closes the game window.
- `play()`: Starts the game by prompting for a bet.

### GUI Components

- `main_window`: The main window of the application.
- `card_frame`: Frame to hold card images.
- `button_frame`: Frame to hold the control buttons.
- Various labels and buttons to display scores, balance, and control the game flow.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- The Python Software Foundation for Python.
- The Tkinter library for the GUI.
- The Pillow library for image handling.

Enjoy the game!
