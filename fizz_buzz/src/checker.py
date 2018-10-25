'''
Simple module that checks whether an integer complies with either the
fizz rule or the buzz rule.
'''

class Checker:
    '''
    Checker class contains two methods is_fizz and is_buzz that return booleans
    dependent on whether an integer complies with either the fizz or buzz rule
    '''

    @staticmethod
    def is_fizz(number):
        '''
        Fizz rule will return True if an integer is divisible by 3
        '''

        return number % 3 == 0

    @staticmethod
    def is_buzz(number):
        '''
        Buzz rule will return True if an integer is divisible by 5
        '''

        return number % 5 == 0
