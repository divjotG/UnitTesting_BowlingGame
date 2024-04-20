import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_game_initialization(self):
        self.assertEqual(len(self.game.rolls), 0)

    def test_gutter_game(self):
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 16)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)

    def test_all_fives(self):
        self.roll_many(5, 21)
        self.assertEqual(self.game.score(), 150)

    def roll_many(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
