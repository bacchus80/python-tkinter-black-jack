import tkinter as tk
from time import sleep
from cards import Deck

# For coherent card spacing
CARD_SPACING = 2

TEXT = {
    "dealer": "Dealer",
    "player": "Player",
    "total": "Total",
    "dealer_busted": "Dealer busted. You win!",
    "you_win": "You win!",
    "dealer_wins": "Dealer wins",
    "tie": "Tie",
    "hit_or_stand": "Hit or stand",
    "your_busted_game_over": "Your busted, game over",
    "hit": "Hit",
    "stand": "Stand",
    "new_game": "New game"
}

# Back Jack game board
class BlackjackBoard:
    def __init__(self, root):
        self.root = root
        self.MAX_VALUE = 21

        self.deck_of_cards = []
        self.player_hand = []
        self.dealer_hand = []

        # Setting up GUI
        self.status_header_text = tk.Label(root,text="", font=("Helvetica, Arial", 28) )
        self.status_header_text.pack(pady=24)

        self.label_dealer = tk.Label(root, text=TEXT['dealer'])
        self.label_dealer.pack()
        self.label_dealer_hand = tk.Label(root, text="")
        self.label_dealer_hand.pack()

        self.label_spacer = tk.Label(root, text="")
        self.label_spacer.pack(pady=0)

        self.label_player = tk.Label(root, text=TEXT['player'])
        self.label_player.pack()
        self.label_player_hand = tk.Label(root, text="")
        self.label_player_hand.pack()

        # Game buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=16)
        self.button_hit = tk.Button(self.button_frame, text=TEXT['hit'], command=self.player_hit)
        self.button_hit.grid(row=0, column=0, padx=2)
        self.button_stand = tk.Button(self.button_frame, text=TEXT['stand'], command=self.player_stand)
        self.button_stand.grid(row=0, column=1, padx=2)
        self.button_reset = tk.Button(self.button_frame, text=TEXT['new_game'], command=self.start_game)
        self.button_reset.grid(row=0, column=2)

        self.start_game()

    def start_game(self):
        """
        Staring a new game, shuffle card
        """
        self.deck_of_cards = Deck()
        self.deck_of_cards.shuffle()

        self.status_header_text.config(text=TEXT['hit_or_stand'])
        self.player_hand = self.deck_of_cards.draw(2)
        self.dealer_hand = self.deck_of_cards.draw(2)

        self.button_hit.config(state=tk.NORMAL)
        self.button_stand.config(state=tk.NORMAL)
        
        self.update_gui(firstDeal=True)

    def player_hit(self):
        """
        Player continue playing
        """
        self.player_hand += self.deck_of_cards.draw(1)
        self.update_gui(firstDeal=True)

        sum_player_hand = self.deck_of_cards.calculate_hand(self.player_hand)
        if sum_player_hand > self.MAX_VALUE:
            self.game_ended(TEXT['your_busted_game_over'])

    def game_ended(self, status_text):
        """
        Game is ended, set header text
        """
        self.disable_buttons()
        self.status_header_text.config(text=status_text)

    def disable_buttons(self):
        """
        Disable "hit" and "stand" buttons
        """
        self.button_hit.config(state=tk.DISABLED)
        self.button_stand.config(state=tk.DISABLED)

    def update_gui(self, firstDeal=False):
        """
        Updates the GUI with total sum and the cards for current round
        """
        sum_player_hand =  str(self.deck_of_cards.calculate_hand(self.player_hand))
        sum_dealer_hand =  str(self.deck_of_cards.calculate_hand(self.dealer_hand))

        if firstDeal:
            dealer_display = TEXT['dealer']
            dealer_display_hand = f"{self.dealer_hand[0]}  [?]"
        else:
            dealer_display = self.get_total_sum_text(TEXT['dealer'], sum_dealer_hand)
            dealer_display_hand = self.format_hand_for_display(self.dealer_hand)

        self.label_dealer.config(text=dealer_display)
        self.label_dealer_hand.config(text=dealer_display_hand)

        player_display = self.get_total_sum_text(TEXT['player'], sum_player_hand)
        self.label_player.config(text=player_display)
        self.label_player_hand.config(text=self.format_hand_for_display(self.player_hand))

    def player_stand(self):
        """
        User clicks "stand" button
        """
        self.disable_buttons()
        self.update_gui(firstDeal=False)
        self.dealer_turn()

    def dealer_turn(self):
        """
        Draws a new card to the dealer until someone wins
        Dealer mush draw a card as long as the hands value is less than 17
        """
        # update dealers card before entering while loop
        self.update_gui(firstDeal=False)

        while self.deck_of_cards.calculate_hand(self.dealer_hand) < 17:
            self.dealer_hand += self.deck_of_cards.draw(1)

            # Force GUI to refresh
            self.root.update_idletasks()
            self.root.update()

            self.update_gui(firstDeal=False)
            self.check_winner()
            sleep(1)

        self.check_winner()

    def check_winner(self):
        """
        Checks who is the winner and update header text
        """
        value_player_hand = self.deck_of_cards.calculate_hand(self.player_hand)
        value_dealer_hand = self.deck_of_cards.calculate_hand(self.dealer_hand)

        if value_dealer_hand > self.MAX_VALUE:
            self.game_ended(TEXT['dealer_busted'])
        elif value_player_hand > value_dealer_hand:
           self.game_ended(TEXT['you_win'])
        elif value_player_hand < value_dealer_hand:
           self.game_ended(TEXT['dealer_wins'])
        else:
            self.game_ended(TEXT['tie'])

    def get_total_sum_text(self, player_name, sum_hand):
        """
        Get total sum for player_name, "player_name (Total: sum_hand)"
        """
        return f"{player_name} ({TEXT['total']}: {sum_hand})"
    
    def format_hand_for_display(self, cards):
        """
        Format players hand for proper display
        """
        return ', '.join(str(card) for card in cards)
