import unittest
from unittest.mock import Mock
from kata_chooser import *

class BerlinClockTest(unittest.TestCase):
	def setUp(self):
		self.mock_chooser = KataChooser()
		self.mock_chooser.random_language = Mock(return_value=3)
		self.mock_chooser.random_question = Mock(return_value=3)

	def test_random_language_should_between_0_to_7(self):
		self.assertTrue(0 <= KataChooser().random_language() <= 7)

	def test_random_question_should_between_0_to_4(self):
		self.assertTrue(0 <= KataChooser().random_question() <= 21)

	def test_choose_language_should_JAVA(self):
		self.assertEqual("Ruby", self.mock_chooser.choose_language())

	def test_choose_question_should_bowling_game(self):
		self.assertEqual("Bowling Game", self.mock_chooser.choose_question())

	def test_chooser_should_kata_bowling_game_with_ruby(self):
		self.assertEqual("Kata: Bowling Game \nWith: Ruby", self.mock_chooser.chooser())