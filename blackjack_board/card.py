DRESSED_CARDS = {
    'Ace': 'Ace',
    'Jack': 'Jack',
    'Queen': 'Queen',
    'King': 'King',
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
    
    def value(self):
        """
        Get the value from the rank
        """
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7,
            '8':8, '9': 9, '10': 10, 
            DRESSED_CARDS['Jack']: 10, 
            DRESSED_CARDS['Queen']: 10, 
            DRESSED_CARDS['King']: 10
        }
        return card_values.get(self.rank, 1)
