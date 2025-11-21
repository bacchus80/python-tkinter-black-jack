import unittest
from blackjack_board.card import Card

class TestCard(unittest.TestCase):
  
  def test_card_init(self):
    card = Card('Clubs', '3')
    self.assertEqual(card.rank, '3')
    self.assertEqual(card.suit, 'Clubs')

  def test_card_init_dressed_card(self):
    card = Card('Spades', 'Queen')
    self.assertEqual(card.rank, 'Queen')
    self.assertEqual(card.suit, 'Spades')

  def test_card_values(self):
      self.assertEqual(Card('Hearts', 'Queen').value(), 10)
      self.assertEqual(Card('Diamonds', '5').value(), 5)
      self.assertEqual(Card('Clubs', 'Jack').value(), 10)
      self.assertEqual(Card('Spades', '9').value(), 9)

  def test_card_representation(self):
      card = Card("Hearts", "2")
      self.assertEqual(str(card), "2 of Hearts")
      
      card = Card("Clubs", "Jack")
      self.assertEqual(str(card), "Jack of Clubs")


  
if __name__ == '__main__':
    unittest.main()
