import random
import tkinter as tk
from PIL import Image, ImageTk
import os

# Constants for card suits, ranks, and values
SUITS = ['hearts', 'clubs', 'diamonds', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
CARD_VALUES = {str(i): i for i in range(2, 11)}
CARD_VALUES.update({'jack': 10, 'queen': 10, 'king': 10, 'ace': 11})

def load_images(card_images):
    """
    Load images for each suit and rank, resize them, and add them to the card_images list.
    """
    for suit in SUITS:
        for rank in RANKS:
            name = f'card_images/{rank}_of_{suit}.png'
            if os.path.exists(name):
                image = Image.open(name)
                image = image.resize((image.width // 4, image.height // 4), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                card_value = CARD_VALUES[rank]
                card_images.append((card_value, photo))
            else:
                print(f"File not found: {name}")

def deal_card(frame):
    """
    Deal the next card from the deck and add it to the given frame.
    """
    next_card = deck.pop(0)
    deck.append(next_card)
    tk.Label(frame, image=next_card[1], relief="raised", bg="#0B6623").grid(row=0, column=len(frame.grid_slaves()), padx=5)
    return next_card

def calculate_points(hand):
    """
    Calculate the score of a hand.
    """
    points = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 11 and not ace:
            ace = True
        points += card_value
        if points > 21 and ace:
            points -= 10
            ace = False
    return points

def dealer_plays():
    """
    Dealer draws cards until the score is at least 17, then determines the result of the game.
    """
    dealer_points = calculate_points(dealer_hand)
    while 0 < dealer_points < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_points = calculate_points(dealer_hand)
        dealer_points_label.set(dealer_points)

    determine_winner()

def player_hits():
    """
    Player draws a card and checks if they have busted.
    """
    player_hand.append(deal_card(player_card_frame))
    player_points = calculate_points(player_hand)
    player_points_label.set(player_points)
    if player_points > 21:
        result_text.set("Dealer wins!")
        update_balance(False)
        end_round()

def initial_deal():
    """
    Deal the initial two cards to the player and one to the dealer.
    """
    player_hits()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_points_label.set(calculate_points(dealer_hand))
    player_hits()

def new_round():
    """
    Start a new round by resetting the hands and updating the UI.
    """
    global dealer_card_frame, player_card_frame, dealer_hand, player_hand

    reset_frames()

    result_text.set("")
    dealer_hand = []
    player_hand = []

    ask_for_bet()

def reset_frames():
    """
    Reset the frames for dealer and player cards.
    """
    global dealer_card_frame, player_card_frame

    for widget in dealer_card_frame.winfo_children():
        widget.destroy()

    for widget in player_card_frame.winfo_children():
        widget.destroy()

def shuffle_deck():
    """
    Shuffle the deck.
    """
    random.shuffle(deck)

def update_balance(player_wins):
    """
    Update the player's balance based on whether they won or lost.
    """
    global balance
    if player_wins:
        balance += bet
    else:
        balance -= bet
    balance_label.set(f"{balance} CHF")

def ask_for_bet():
    """
    Prompt the player to enter their bet.
    """
    bet_label.set("Enter your bet:")
    bet_entry.grid(row=3, column=3, pady=10)
    bet_button.grid(row=5, column=2, pady=10)

def place_bet():
    """
    Place the player's bet and start the initial deal.
    """
    global bet
    try:
        bet = int(bet_entry.get())
        if bet > balance or bet <= 0:
            bet_label.set("Invalid bet amount!")
        else:
            bet_label.set(f"Bet: {bet} CHF")
            bet_entry.grid_forget()
            bet_button.grid_forget()
            player_button.config(state="normal")
            dealer_button.config(state="normal")
            initial_deal()
    except ValueError:
        bet_label.set("Please enter a valid number!")

def determine_winner():
    """
    Determine the winner and update the balance.
    """
    player_points = calculate_points(player_hand)
    dealer_points = calculate_points(dealer_hand)
    if player_points > 21:
        result_text.set("Dealer wins!")
        update_balance(False)
    elif dealer_points > 21 or dealer_points < player_points:
        result_text.set("Player wins!")
        update_balance(True)
    elif dealer_points > player_points:
        result_text.set("Dealer wins!")
        update_balance(False)
    else:
        result_text.set("Draw!")
    end_round()

def end_round():
    """
    End the current round and enable the appropriate buttons.
    """
    player_button.config(state="disabled")
    dealer_button.config(state="disabled")
    new_round_button.config(state="normal")
    leave_button.config(state="normal")

def leave_table():
    """
    Display a message with the player's balance and enable the end game button.
    """
    result_text.set(f"Congratulations, your balance is {balance} CHF")
    leave_button.config(state="disabled")
    end_game_button.grid(row=5, column=3, pady=10)

def end_game():
    """
    Close the game window.
    """
    main_window.destroy()

def play():
    """
    Start the game by prompting for a bet.
    """
    ask_for_bet()
    main_window.mainloop()

# Set up the main window
main_window = tk.Tk()
main_window.title("Black Jack")
main_window.geometry("800x600")
main_window.configure(bg="#0B6623")  # Dark green

# Configure grid layout for the main window
main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=2)
main_window.columnconfigure(3, weight=0)
main_window.columnconfigure(4, weight=5)
main_window.columnconfigure(5, weight=0)

# Result label to display game outcome
result_text = tk.StringVar()
result = tk.Label(main_window, textvariable=result_text, font=("Helvetica", 16, "bold"), bg="#0B6623", fg="#FFFFFF")  # White text
result.grid(row=0, column=0, columnspan=3, pady=10)

# Frame to hold card images
card_frame = tk.Frame(main_window, relief="sunken", borderwidth=1, bg="#228B22")  # Forest green
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2, pady=10, padx=10)

# Labels for dealer's score and cards
dealer_points_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", bg="#228B22", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=5)  # White text
tk.Label(card_frame, textvariable=dealer_points_label, bg="#228B22", fg="#FFFFFF", font=("Helvetica", 12)).grid(row=1, column=0, pady=5)  # White text
dealer_card_frame = tk.Frame(card_frame, bg="#228B22")  # Forest green
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# Labels for player's score and cards
player_points_label = tk.IntVar()
tk.Label(card_frame, text="Player", bg="#228B22", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=2, column=0, pady=5)  # White text
tk.Label(card_frame, textvariable=player_points_label, bg="#228B22", fg="#FFFFFF", font=("Helvetica", 12)).grid(row=3, column=0, pady=5)  # White text
player_card_frame = tk.Frame(card_frame, bg="#228B22")  # Forest green
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Frame to hold buttons
button_frame = tk.Frame(main_window, bg="#0B6623")  # Dark green
button_frame.grid(row=4, column=0, columnspan=5, pady=10, padx=10)

# Buttons for game actions
player_button = tk.Button(button_frame, text="Hit", command=player_hits, padx=8, state="disabled", bg="#FFD700", fg="#000000", font=("Helvetica", 12, "bold"))  # Gold button, black text
player_button.grid(row=0, column=0, padx=5)

dealer_button = tk.Button(button_frame, text="Stay", command=dealer_plays, padx=5, state="disabled", bg="#FFD700", fg="#000000", font=("Helvetica", 12, "bold"))  # Gold button, black text
dealer_button.grid(row=0, column=1, padx=5)

new_round_button = tk.Button(button_frame, text="New Round", command=new_round, state="disabled", bg="#32CD32", fg="#000000", font=("Helvetica", 12, "bold"))  # Lime green button, black text
new_round_button.grid(row=0, column=2, padx=5)

bet_button = tk.Button(button_frame, text="Place Bet", command=place_bet, bg="#FFD700", fg="#000000", font=("Helvetica", 12, "bold"))  # Gold button, black text
bet_button.grid(row=1, column=2, padx=5)

leave_button = tk.Button(button_frame, text="Leave Table and Take Money", command=leave_table, bg="#FF4500", fg="#000000", font=("Helvetica", 12, "bold"))  # Orange red button, black text
leave_button.grid(row=1, column=0, columnspan=2, pady=10)

end_game_button = tk.Button(main_window, text="Close Program", command=end_game, bg="#DC143C", fg="#000000", font=("Helvetica", 12, "bold"))  # Crimson button, black text
end_game_button.grid(row=5, column=3, pady=10)
end_game_button.grid_remove()

# Load card images
cards = []
load_images(cards)

# Create and shuffle the deck
deck = list(cards) + list(cards) + list(cards)
shuffle_deck()

# Initialize player and dealer hands
dealer_hand = []
player_hand = []

# Set initial balance and bet
balance = 1000
bet = 0

# Label for displaying balance
balance_label = tk.StringVar()
balance_label.set(f"{balance} CHF")
tk.Label(main_window, text="Balance", bg="#0B6623", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=0, column=3, pady=10)  # White text
tk.Label(main_window, textvariable=balance_label, bg="#0B6623", fg="#FFFFFF", font=("Helvetica", 12)).grid(row=1, column=3)  # White text

# Label and entry for placing bets
bet_label = tk.StringVar()
bet_label.set("Enter your bet:")
tk.Label(main_window, textvariable=bet_label, bg="#0B6623", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=2, column=3, pady=10)  # White text

bet_entry = tk.Entry(main_window, font=("Helvetica", 12), bg="#FFFFFF", fg="#000000")  # White entry, black text

if __name__ == "__main__":
    play()
