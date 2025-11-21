# Imaging Library for displaying cards
from PIL import ImageTk, Image
import random
from blackjack_board.card import Card

DRESSED_CARDS = {
    'Ace': 'Ace',
    'Jack': 'Jack',
    'Queen': 'Queen',
    'King': 'King',
}


class Deck:
    """
    A deck of cards
    """

    # Image variables
    card_dimension = [109, 160] # size for one card in a image [width, height] 
    cards_path = 'assets/cards.png'
    card_fAced_down_path = 'assets/card-back.png'

    # order suits and rank matching image with cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
    ranks = [DRESSED_CARDS['Ace'],'2', '3', '4', '5', '6', '7', '8', '9', '10',
             DRESSED_CARDS['Jack'], DRESSED_CARDS['Queen'], DRESSED_CARDS['King']]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        """
        Shuffle the deck of cards
        """
        random.shuffle(self.cards)

    def draw(self, n=1):
        """
        Draw n number of cards from the deck
        """
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        
        return drawn
    
    def calculate_hand(self, hand):
        """
        Calculate value of the hand for Black Jack
        """
        value = 0
        Aces = 0

        for card in hand:
            if card.rank == DRESSED_CARDS['Ace']:
                Aces += 1
                value += 11
            else:
                value += card.value()

        while value > 21 and Aces > 0:
            value -= 10
            Aces -= 1

        return value

    def get_card_face(self, card):
        """
        Get a card image for the suit and rank
        """
        # image containing 52 cards, every suit on its on row
        card_image = Image.open(self.cards_path)
        row = self.suits.index(card.suit)
        card_value = self.ranks.index(card.rank)+1

        # get correct card from the image
        # extracting positions for better readability
        pos_x1 = self.card_dimension[0] * (card_value - 1)
        pos_y1 = self.card_dimension[1] * row
        pos_x2 = self.card_dimension[0] * card_value
        pos_y2 = self.card_dimension[1] * (row + 1)

        cropped = card_image.crop((pos_x1, pos_y1, pos_x2, pos_y2))

        return ImageTk.PhotoImage(cropped)

    def get_card_faced_down(self):
      """
      Get image of a card fAced down (for dealer)
      """
      return ImageTk.PhotoImage(Image.open(self.card_fAced_down_path))