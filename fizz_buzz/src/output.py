from fizz_buzz.src.checker import Checker

class Output:

    @staticmethod
    def get_fizz_buzz(number):

        if Checker.is_fizz(number) and Checker.is_buzz(number):
            return 'FizzBuzz'

        if Checker.is_fizz(number):
            return 'Fizz'

        if Checker.is_buzz(number):
            return 'Buzz'

        return str(number)
