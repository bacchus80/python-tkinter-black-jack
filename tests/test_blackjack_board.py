import unittest
from unittest.mock import MagicMock, patch
from blackjack_board.deck import DRESSED_CARDS

# Helper methot to create fake cards
def fake_card(suit, rank):
  card = MagicMock()
  card.rank = rank
  card.suit = suit
  card.value.return_value = 10 if rank in ['Jack', 'Queen', 'King'] else (11 if rank == 'Ace' else int(rank))
  return card  

def mock_calculate_hand(hand):
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

class TestBlackjackBoard(unittest.TestCase):

  def setUp(self):
      """
      Patch Deck, Scoreboard and Blackjack board 
      """
      # Patch Deck where blackjack_board.py imports a Deck
      deck_patcher = patch("blackjack_board.blackjack_board.Deck")
      self.MockDeck = deck_patcher.start()
      self.addCleanup(deck_patcher.stop)
      
      # Patch scoreboard
      scoreboard_patcher = patch("blackjack_board.blackjack_board.ScoreBoard")
      self.MockScoreBoard = scoreboard_patcher.start()
      self.addCleanup(scoreboard_patcher.stop)
      self.mock_scoreboard = self.MockScoreBoard.return_value

      # Replace the real scoreboard instance with a mock
      self.mock_scoreboard = self.MockScoreBoard.return_value

      # Create the mock instance of Deck
      self.mock_deck = self.MockDeck.return_value

      root_patcher = patch("tkinter.Tk")
      self.MockTk = root_patcher.start()
      self.addCleanup(root_patcher.stop)

      self.root = self.MockTk()

      from blackjack_board.blackjack_board import BlackjackBoard
      self.board_class = BlackjackBoard

      # Create board instance
      self.board = self.board_class(self.root)

      # GUI requires this
      self.mock_deck.get_card_face.return_value = MagicMock()
      self.mock_deck.get_card_faced_down.return_value = MagicMock()

      self.board.status_header_text = MagicMock()
      self.board.status_header_text.config = MagicMock()

  def test_player_wins(self):
    # fake cards
    cards = [
        fake_card('Hearts','Jack'),# Player card 1
        fake_card('Clubs', '7'),# Player card 2
        fake_card('Spades','9'), # Dealer card 1
        fake_card('Diamonds','5'), # Dealer card 2
        fake_card('Hearts', '3'),
        fake_card('Clubs', 'Queen'),
        fake_card('Diamonds', 'Ace'),
        fake_card('Spades', '2'),
    ]

    self.board.deck_of_cards.draw.side_effect = lambda n: [cards.pop(0) for _ in range(n)]

    self.board.deck_of_cards.calculate_hand.side_effect = mock_calculate_hand

    # Start the game
    self.board.start_game()

    # Simulate player standing
    self.board.player_hit()
    self.board.player_stand()

    # Assertions
    self.board.status_header_text.config.assert_called_with(text="Dealer busted. You win!")
    self.mock_scoreboard.update_score_player_wins.assert_called_once()

  def test_dealer_wins(self):
    # fake cards
    cards = [
        fake_card('Hearts','4'), # Player card 1
        fake_card('Clubs', '6'), # Player card 2
        fake_card('Spades','9'), # Dealer card 1
        fake_card('Diamonds','5'), # Dealer card 2
        fake_card('Hearts', '10'),
        fake_card('Clubs', '7'),
        fake_card('Diamonds', 'Ace'),
        fake_card('Spades', '2'),
    ]

    self.board.deck_of_cards.draw.side_effect = lambda n: [cards.pop(0) for _ in range(n)]

    self.board.deck_of_cards.calculate_hand.side_effect = mock_calculate_hand

    # Start the game
    self.board.start_game()

    # Simulate player standing
    self.board.player_hit()
    self.board.player_stand()

    # Assertions
    self.board.status_header_text.config.assert_called_with(text="Dealer wins")
    self.mock_scoreboard.update_score_player_loses.assert_called_once()

  def test_tie(self):
    # fake cards
    cards = [
        fake_card('Hearts','Jack'), # Player card 1
        fake_card('Clubs', '7'), # Player card 2
        fake_card('Spades','9'),# Dealer card 1
        fake_card('Diamonds','5'), # Dealer card 2
        fake_card('Hearts', '3'),
        fake_card('Clubs', '6'),
        fake_card('Diamonds', 'Ace'),
        fake_card('Spades', '2'),
    ]

    self.board.deck_of_cards.draw.side_effect = lambda n: [cards.pop(0) for _ in range(n)]

    self.board.deck_of_cards.calculate_hand.side_effect = mock_calculate_hand

    # Start the game
    self.board.start_game()

    # Simulate player standing
    self.board.player_hit()
    self.board.player_stand()

    # Assertions
    self.board.status_header_text.config.assert_called_with(text="Tie")
    self.mock_scoreboard.update_score_tie.assert_called_once()
    
  def test_evaluate_hand_with_ace(self):
    # fake cards
    cards = [
        fake_card('Hearts','3'), # Player card 1
        fake_card('Clubs', 'Ace'), # Player card 2
        fake_card('Spades','9'),# Dealer card 1
        fake_card('Diamonds','5'), # Dealer card 2
        fake_card('Hearts', 'Queen'),
        fake_card('Clubs', '6'),
        fake_card('Diamonds', 'Ace'),
        fake_card('Spades', '2'),
    ]

    self.board.deck_of_cards.draw.side_effect = lambda n: [cards.pop(0) for _ in range(n)]

    self.board.deck_of_cards.calculate_hand.side_effect = mock_calculate_hand

    # Start the game
    self.board.start_game()

    player_hand_value = self.board.deck_of_cards.calculate_hand(self.board.player_hand)
    self.assertEqual(player_hand_value, 14)

    self.board.player_hit()
    
    player_hand_new_value = self.board.deck_of_cards.calculate_hand(self.board.player_hand)
    self.assertEqual(player_hand_new_value, 14)
   
if __name__ == '__main__':
    unittest.main()
