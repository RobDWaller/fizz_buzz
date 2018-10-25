import unittest
from fizz_buzz.src.output import Output

class TestOutput(unittest.TestCase):

    def test_is_fizz(self):

        self.assertEqual(Output.get_fizz_buzz(3), 'Fizz')

    def test_is_buzz(self):

        self.assertEqual(Output.get_fizz_buzz(5), 'Buzz')

    def test_is_fizz_buzz(self):

        self.assertEqual(Output.get_fizz_buzz(15), 'FizzBuzz')

    def test_is_number(self):

        self.assertEqual(Output.get_fizz_buzz(4), '4')
