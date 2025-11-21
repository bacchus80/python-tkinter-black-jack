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
"""

class TestCalculator(unittest.TestCase):

  def setUp(self):
    # This method will run before each test
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.add(2,3),5, "Incorrect sum")
    self.assertEqual(self.calculator.add(2,-3), -1, "Incorrect sum")
  
  def test_subtraction(self):
    self.assertEqual(self.calculator.subtract(5, 2), 3, "Incorrect subtraction")
    self.assertEqual(self.calculator.subtract(2, 5), -3, "Incorrect subtraction")
    self.assertEqual(self.calculator.subtract(2, -5), 7, "Incorrect subtraction")

  def test_multiplication(self):
     self.assertEqual(self.calculator.multiply(2, 4), 8)
     self.assertEqual(self.calculator.multiply(2, 0), 0)
     self.assertEqual(self.calculator.multiply(2, -3), -6)

  def test_division(self):
     self.assertEqual(self.calculator.divide(4, 2), 2)
     self.assertEqual(self.calculator.divide(2, 4), 0.5)
     self.assertEqual(self.calculator.divide(-4, 2), -2)
     self.assertEqual(self.calculator.divide(8, -2), -4)
     self.assertEqual(self.calculator.divide(0, 0.5), 0)

     with self.assertRaises(ZeroDivisionError):
        self.calculator.divide(10,0)

  def test_square(self):
     self.assertEqual(self.calculator.square(3), 9)
     self.assertEqual(self.calculator.square(-4), 16)
     self.assertEqual(self.calculator.square(0.5), 0.25)

  def test_power(self):
     self.assertEqual(self.calculator.power(2, 3), 8)
     self.assertEqual(self.calculator.power(-2, 3), -8)
     self.assertEqual(self.calculator.power(5, 0), 1)

  

  if __name__ == '__main__':
      unittest.main()
"""