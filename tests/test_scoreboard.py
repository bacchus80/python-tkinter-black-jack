import unittest
import tkinter as tk
from blackjack_board.scoreboard import ScoreBoard

class TestScoreboard(unittest.TestCase):

  def setUp(self):
    root = tk.Tk()
    self.score_board = ScoreBoard(root)
    return super().setUp()

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
