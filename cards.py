import random

DRESSED_CARDS = {
    'ace': 'Ace',
    'jack': 'Jack',
    'queen': 'Queen',
    'king': 'King',
}

class Card:
    """
    A playing card, a suit and rank (value)
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    """
    A deck of cards
    """

    # order suits and rank matching image with cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
    ranks = [DRESSED_CARDS['ace'],'2', '3', '4', '5', '6', '7', '8', '9', '10',
             DRESSED_CARDS['jack'], DRESSED_CARDS['queen'], DRESSED_CARDS['king']]

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
        Calculate value of the hand for Black jack
        """
        value = 0
        aces = 0

        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7,
            '8':8, '9': 9, '10': 10, 
            DRESSED_CARDS['jack']: 10, 
            DRESSED_CARDS['queen']: 10, 
            DRESSED_CARDS['king']: 10
        }

        for card in hand:
            if card.rank == DRESSED_CARDS['ace']:
                aces += 1
                value += 11
            else:
                value += card_values.get(card.rank, 1)

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value
    