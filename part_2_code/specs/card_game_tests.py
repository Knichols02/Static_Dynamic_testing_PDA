import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame("Game")

        self.card1 = Card("hearts", 2)
        self.card2 = Card("diamonds", 6)
        self.card3 = Card("clubs", 8)
        self.card4 = Card("spades", 1)

        self.hand = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace_card(self):
        self.assertEqual(True, self.game.check_for_ace(self.card4))

    def test_check_for_card_not_ace(self):
        self.assertEqual(False, self.game.check_for_ace(self.card2))

    def test_check_for_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 17", self.game.cards_total(self.hand))
   