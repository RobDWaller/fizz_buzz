import unittest
from fizz_buzz.src.checker import Checker

class TestChecker(unittest.TestCase):

    def test_is_fizz(self):

        self.assertTrue(Checker.is_fizz(3))

    def test_is_not_fizz(self):

        self.assertFalse(Checker.is_fizz(4))

    def test_is_buzz(self):

        self.assertTrue(Checker.is_buzz(5))

    def test_is_not_buzz(self):

        self.assertFalse(Checker.is_buzz(7))
