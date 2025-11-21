import unittest
from unittest.mock import patch
from blackjack_board.scoreboard import ScoreBoard

class TestScoreboard(unittest.TestCase):

  @patch("tkinter.Tk")
  def setUp(self, MockTk):
    # Mock window
    root = MockTk()
    self.score_board = ScoreBoard(root)

  def test_initial_scores(self):
    self.assertEqual(self.score_board.nr_of_losses, 0)
    self.assertEqual(self.score_board.nr_of_ties, 0)
    self.assertEqual(self.score_board.nr_of_wins, 0)

  def test_update_player_wins(self):
    self.score_board.update_score_player_wins()
    self.assertEqual(self.score_board.nr_of_wins, 1)

  def test_update_dealer_wins(self):
    self.score_board.update_score_player_loses()
    self.assertEqual(self.score_board.nr_of_losses, 1)

  def test_update_tie(self):
    self.score_board.update_score_tie()
    self.assertEqual(self.score_board.nr_of_ties, 1)


if __name__ == '__main__':
    unittest.main()
