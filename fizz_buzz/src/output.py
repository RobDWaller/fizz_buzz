'''
Simple module to generate output for FizzBuzz test
'''

from fizz_buzz.src.checker import Checker

class Output: # pylint: disable=too-few-public-methods
    '''
    Output class contains single method that returns fizz buzz result based on
    the inputed number
    '''

    @staticmethod
    def get_fizz_buzz(number):
        '''
        Static method that consumers an integer then checks which fizz buzz
        rule the integer complies with.
        Returns a string:
        FizzBuzz if integer is divisible by 3 and 5
        Fizz if integer is divisible by 3
        Buzz if integer is divisible by 5
        Integer as string if neither divisible by 3 nor 5
        '''

        if Checker.is_fizz(number) and Checker.is_buzz(number):
            return 'FizzBuzz'

        if Checker.is_fizz(number):
            return 'Fizz'

        if Checker.is_buzz(number):
            return 'Buzz'

        return str(number)
